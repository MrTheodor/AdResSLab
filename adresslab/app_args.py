"""
Copyright (C) 2017 Jakub Krajniak <jkrajniak@gmail.com>

This file is distributed under free software licence:
you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import tools as general_tools
import random
import ast


def _args_md():
    parser = general_tools.MyArgParser(description='Runs AdResS simulation',
                                       fromfile_prefix_chars='@')
    parser.add_argument('--conf', required=True, help='Input .gro coordinate file')
    parser.add_argument('--top', '--topology', required=True, help='Topology file',
                        dest='top')
    parser.add_argument('--node_grid')
    parser.add_argument('--cell_grid')
    parser.add_argument('--skin', type=float, default=0.16,
                        help='Skin value for Verlet list')
    parser.add_argument('--run', type=int, default=10000,
                        help='Number of simulation steps')
    parser.add_argument('--int_step', default=1000, type=int, help='Steps in integrator loop')
    parser.add_argument('--dt', default=0.001, type=float,
                        help='Integrator time step')
    parser.add_argument('--rng_seed', type=int, help='Seed for RNG', required=False,
                        default=random.randint(1000, 10000))
    parser.add_argument('--output_prefix',
                        default='sim', type=str,
                        help='Prefix for output files')
    parser.add_argument('--energy_collect', default=1000, help='How often collect energy terms', type=int)

    misc_group = parser.add_argument_group('Misc')
    parser.add_argument('--remove_com', type=ast.literal_eval, help='Removes total velocity of the system', default=False)
    misc_group.add_argument('--cap_force', type=float, help='Define maximum cap-force in the system')

    thermostat_group = parser.add_argument_group('Thermostat')
    thermostat_group.add_argument('--thermostat',
                        default='lv',
                        choices=('lv', 'vr'),
                        help='Thermostat to use, lv: Langevine, vr: Stochastic velocity rescale')
    thermostat_group.add_argument('--thermostat_gamma', type=float, default=0.5,
                        help='Thermostat coupling constant')
    thermostat_group.add_argument('--temperature', default=298.0, type=float, help='Temperature')

    barostat_group = parser.add_argument_group('Barostat')
    barostat_group.add_argument('--barostat', default='lv', choices=('lv', 'br'),
                        help='Barostat to use, lv: Langevine, br: Berendsen')
    barostat_group.add_argument('--barostat_tau', default=5.0, type=float,
                        help='Tau parameter for Berendsen barostat')
    barostat_group.add_argument('--barostat_mass', default=50.0, type=float,
                        help='Mass parameter for Langevin barostat')
    barostat_group.add_argument('--barostat_gammaP', default=1.0, type=float,
                        help='gammaP parameter for Langevin barostat')
    barostat_group.add_argument('--pressure', help='Pressure', type=float)

    interactions_group = parser.add_argument_group('Interactions')
    interactions_group.add_argument('--cutoff', default=1.2, type=float,
                        help='Cutoff of atomistic non-bonded interactions')
    interactions_group.add_argument('--coulomb_epsilon1', default=1.0, type=float,
                        help='Epsilon_1 for coulomb interactions')
    interactions_group.add_argument('--coulomb_epsilon2', default=78.0, type=float,
                        help='Epsilon_2 for coulomb interactions')
    interactions_group.add_argument('--coulomb_kappa', default=0.0, type=float,
                        help='Kappa paramter for coulomb interactions')
    interactions_group.add_argument('--coulomb_cutoff', default=0.9, type=float,
                        help='Cut-off for generalized reactive coulomb reactions')
    interactions_group.add_argument('--table_groups', default=None,
                        help='Name of CG groups to read from tables')
    interactions_group.add_argument('--exclusion_list', default=None, help='The exclusion list')

    adress_group = parser.add_argument_group('AdResS settings')
    adress_group.add_argument('--adress_ex', help='Size of explicit region', type=float, required=True)
    adress_group.add_argument('--adress_hy', help='Size of hybrid region', type=float, required=True)
    adress_group.add_argument(
        '--adress_centre', default='box_centre',
        help='Where is the centre of explicit region. Format: "box_centre" - for box centre; x,y,z - specific position.')
    adress_group.add_argument('--adress_use_sphere', help='If True then spherical AdResS is used', default=False,
                              type=ast.literal_eval)

    em_group = parser.add_argument_group('Energy minimization')
    em_group.add_argument('--em', help='Maximum number of steps to perform in EM', type=int, default=0)
    em_group.add_argument('--em_gamma', help='Gamma parameter for force damping', type=float, default=0.0001)
    em_group.add_argument('--em_ftol', help='Force tolerance', type=float, default=10.0)
    em_group.add_argument('--em_max_d', help='Max displacement x box dimension', default=0.001, type=float)

    return parser