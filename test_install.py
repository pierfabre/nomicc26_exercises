#!/usr/bin/env python
import argparse

import casadi as ca
import numpy as np

def test_nosnoc():
    import nosnoc
    from vdx.vartypes import Primal, Constraint, CConstraint
    from nosnoc.mpccsol.plugins.reg_homotopy import RegHomotopyOptions
    mpcc = nosnoc.MPCC()
    mpcc.w.x[1] = Primal("x1", 1, lb=0, ub=np.inf, init=2.0)
    mpcc.w.x[2] = Primal("x2", 1, lb=0, ub=np.inf, init=2.0)

    x1 = mpcc.w.x[1].sym
    x2 = mpcc.w.x[2].sym

    mpcc.g.sumx[()] = Constraint(x1 + 2*x2, lb=-np.inf, ub = 0.5)

    mpcc.G.comp[()] = CConstraint(x1)
    mpcc.H.comp[()] = CConstraint(x2)

    mpcc.f += (x1-1)**2 + (x2-1)**2

    opts = RegHomotopyOptions()

    mpcc.solve(casadi_opts=opts, plugin="reg_homotopy")

    print(f"Solution: x1 = {mpcc.w.x[1].res} x2 = {mpcc.w.x[2].res}")

def test_ccopt(libhsl=False):
    w = ca.SX.sym("x", 2)
    x1 = w[0]
    x2 = w[1]

    g = x1 + 2*x2

    f = (x1-1)**2 + (x2-1)**2

    cc_pairs = np.array([[0,1]])
    cc_types = np.array([0]) # cc_types from libMad: VARVAR 0 VARCON 1 CONVAR 2 CONCON 3

    nlp = {
        "x": w,
        "f": f,
        "g": g,
    }

    casadi_solver_opts = {
        "cc_pairs": cc_pairs.tolist(),
        "cc_types": cc_types.tolist(),
        "print_time": False,
    }
    casadi_solver_opts["ccopt"] = {
        "relaxation_update.TYPE": "RolloffRelaxationUpdate",
        "q_regularization": "critical_rho",
    }
    casadi_solver_opts["madnlp"] = {
        "linear_solver": "Ma27Solver" if libhsl else "MumpsSolver",
        "bound_relax_factor": 0.0,
    }

    ccopt_solver = ca.nlpsol("ccopt_mpcc", "ccopt", nlp, casadi_solver_opts)

    res = ccopt_solver(
        x0=[2.0, 2.0],
        lbx=[0,0],
        ubx=[np.inf, np.inf],
        lbg=[-np.inf],
        ubg=[0.5],
    )

    print(f"Solution: x1 = {res['x'][0]} x2 = {res['x'][1]}")


def test_camino(gurobi=False):
    from camino.problems.problem_collection import create_dummy_problem
    from camino.solver import MinlpSolver, MinlpProblem, MinlpData, Settings, Stats

    problem, data, settings = create_dummy_problem()
    if gurobi:
        stats = Stats("s-b-miqp", "dummy")
        solver = MinlpSolver("s-b-miqp", problem, data, stats, settings)
        result = solver.solve(data)
        solver.stats.print()
    else:
        is_discrete = [1 if i in np.array(problem.idx_x_integer).flatten() else 0 for i in range(problem.x.shape[0])]
        solver = ca.nlpsol(
            "minlp",
            "bonmin",
            {"f": problem.f, "g": problem.g, "x": problem.x, "p": problem.p},
            {"discrete": is_discrete}
        )

        res = solver(x0=data.x0, lbx=data.lbx, ubx=data.ubx, lbg=data.lbg, ubg=data.ubg, p=data.p)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--nosnoc", action="store_true", help="Test nosnoc install")
    parser.add_argument("--ccopt", action="store_true", help="Test ccopt install")
    parser.add_argument("--camino", action="store_true", help="Test camino install")
    parser.add_argument("--gurobi", action="store_true", help="Test gurobi example")
    parser.add_argument("--libhsl", action="store_true", help="Test libhsl example")

    args = parser.parse_args()

    if args.nosnoc:
        test_nosnoc()

    if args.ccopt:
        test_ccopt()

    if args.libhsl:
        test_ccopt(libhsl=True)

    if args.camino:
        test_camino()

    if args.gurobi:
        test_camino(gurobi=True)
