import json
import path_planning as pp

def run_path_planning(scenario_file, navmesh_file, grid_size,
                      algorithm, heuristic, start, finish):
    pp.load_image(scenario_file)
    if navmesh_file:
        with open(navmesh_file) as navmesh:
            path = pp.run_path_planning_mesh(navmesh['mesh'],
                                             algo=algorithm,
                                             heur=heuristic,
                                             start=(
                                                 int(start.replace('(', '').\
                                                     replace(')', '').\
                                                     replace(' ', '').split(',')[0]),
                                                 int(start.replace('(', '').\
                                                     replace(')', '').\
                                                     replace(' ', '').split(',')[1])),
                                             finish=(
                                                 int(finish.replace('(', '').\
                                                     replace(')', '').\
                                                     replace(' ', '').split(',')[0]),
                                                 int(finish.replace('(', '').\
                                                     replace(')', '').\
                                                     replace(' ', '').split(',')[1])))
    else:
        if not grid_size:
            print("Please, define a grid size.")
            exit()
        path = pp.run_path_planning(int(grid_size), algo=algorithm,
                                    heur=heuristic, start=(
                                                 int(start.replace('(', '').\
                                                     replace(')', '').\
                                                     replace(' ', '').split(',')[0]),
                                                 int(start.replace('(', '').\
                                                     replace(')', '').\
                                                     replace(' ', '').split(',')[1])),
                                             finish=(
                                                 int(finish.replace('(', '').\
                                                     replace(')', '').\
                                                     replace(' ', '').split(',')[0]),
                                                 int(finish.replace('(', '').\
                                                     replace(')', '').\
                                                     replace(' ', '').split(',')[1])))
    pp.output_image(scenario_file, path)
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(\
        description='Run path planning using a specified scenario.')
    parser.add_argument('--scenario', metavar='s',\
        help='Path to the image file in which the scenario is defined.', required=True)
    parser.add_argument('--algorithm', metavar='a',\
                        help='String identifier for the algorithm to '\
                        'use. Caps sensitive.', required=True)
    parser.add_argument('--heuristic', metavar='h',\
                        help='String identifier for the heuristic to '\
                        'use. Caps sensitive.', required=True)
    parser.add_argument('--start', metavar='s',\
                        help='Tuple defining the starting point in the '\
                        'scenario.', required=True)
    parser.add_argument('--finish', metavar='f',\
                        help='Tuple defining the finishing point in the '\
                        'scenario.', required=True)
    parser.add_argument('--navmesh', metavar='n',\
                        help='Sets the driver to navmesh mode. '\
                        'Path to the JSON file defining '\
                        'the corresponding navmesh. Use only if not '\
                        'running the algorithm over a grid.')
    parser.add_argument('--grid_size', metavar='g',\
                        help='Integer identifying the number of divisions '\
                        'over the X and Y axis of the scenario. Use only if '\
                        'not using navmesh.')
    parser.add_argument('--version', action='store_true', \
            help='Displays the current version of the simulator')
    args = parser.parse_args()
    if args.version:
        print('v.0.0.1')
        exit()
    if not args.scenario:
        print("No scenario file was defined. Please, provide a scenario file.")
        exit()
    if not args.algorithm:
        print("No algorithm was defined.")
        exit()
    if not args.heuristic:
        print("No heuristic was defined.")
        exit()
    if not args.start:
        print("No starting point was defined.")
        exit()
    if not args.finish:
        print("No finishing point was defined.")
        exit()
    run_path_planning(args.scenario, args.navmesh, args.grid_size,
                      args.algorithm, args.heuristic,
                      args.start, args.finish)
