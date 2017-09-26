"""
Copyright (C) 2017
    Jakub Krajniak (jkrajniak at gmail.com)

This file is part of AdResSLab.

AdResSLab is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

AdResSLab is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


def set_single_th_force(thdforce, input_conf, tf_new):
    """Sets single thermodynamic force for all types of CG particles."""
    for type_id, type_data in input_conf.atomtypeparams.items():
        if type_data['particletype'] == 'V':
            thdforce.addForce(itype=3, filename=tf_new, type=type_id)