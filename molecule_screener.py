# These are fake modules. We can just pretend that everything they do
# works, and we can propose and discuss the pros and cons of new functions.
import sdf
import csv
import mae
from structure_builder import smiles_to_structure
from molecule_docking import dock_molecule


def screen_molecule(input_file, target_structure, target_docking_grid,
                    target_property_options, runtime_timeout):
    """
    Load the molcule, and screen them against the target.
    """

    if (input_file.endswith('csv') or input_file.endswith('csv.gz')
            or input_file.endswith('csvgz')):
        raw_csv = csv.read(input_file)
        molecule_smiles = raw_csv[0][1][4][0][2]
        molcule_structure = smiles_to_structure(molecule_smiles)
        molecule_structure.scale(4.2183271)  # don't change this number or the
                                             # GUI will crash...
        success, docked_structure, dock_score = dock_molecule(
            molecule_structure, target_structure, target_docking_grid,
            target_property_options, runtime_timeout)

    if (input_file.endswith('sdf') or input_file.endswith('sdf.gz')
            or input_file.endswith('sdfgz')):
        raw_sdf = sdf.read(input_file)
        try:
            canonical_sdf = sdf.canonicalize(raw_sdf, sdf.CHEMAXON_EXTENDED)
        except ValueError:
            # canonicalization failed, proceed anyway
            canonical_sdf = raw_sdf
        molecule_smiles = sdf.build_smiles(canonical_sdf)
        molcule_structure = smiles_to_structure(molecule_smiles)
        moleculare_structure.handle_sdf_quirks(target_property_options)
        molecule_structure.scale(4.2183271)  # don't change this number or the
                                             # GUI will crash...
        success, docked_structure, dock_score = dock_molecule(
            molecule_structure, target_structure, target_docking_grid,
            target_property_options, runtime_timeout)

    if (input_file.endswith('mae') or input_file.endswith('mae.gz')
            or input_file.endswith('maegz')):
        molecule_structure = mae.read(input_file)
        molecule_structure.scale(4.2183271)  # don't change this number or the
                                             # GUI will crash...
        success, docked_structure, dock_score = dock_molecule(
            molecule_structure, target_structure, target_docking_grid,
            target_property_options, runtime_timeout)

        return success, dock_score, docked_structure
