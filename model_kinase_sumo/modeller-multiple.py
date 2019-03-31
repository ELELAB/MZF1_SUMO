##comparative modeling with multiple templates
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class

class MyModel(automodel):
    def special_restraints(self, aln):
        rsr = self.restraints
        at = self.atoms
#       Add some restraints 
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['NZ:23:A'],
                                                         at['C:346:C']),
                               mean=1.3, stdev=0.005))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['NZ:149:B'],
                                                         at['C:535:E']),
                               mean=1.3, stdev=0.005))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['NZ:264:C'],
                                                         at['C:442:D']),
                               mean=1.3, stdev=0.005))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['NZ:453:E'],
                                                         at['C:631:F']),
                               mean=1.3, stdev=0.005))
    def select_atoms(self):
        # Select residues 1 and 2 (PDB numbering)
        return selection(self.residue_range('347:D', '442:D'), self.residue_range('147:B', '151:B'), self.residue_range('262:C', '266:C'), self.residue_range('21:A', '25:A'), self.residue_range('452:E', '456:E'), self.residue_range('254:C', '346:C'), self.residue_range('443:E', '535:E'), self.residue_range('536:F', '631:F'))
    
log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']
env.io.hetatm = True
a = MyModel(env,
              alnfile  = 'align2.ali', # alignment filename
              knowns   = ('MZF1_tail_pS8_pS111', '2N1W_0001_copy', '2VRR_1_mod', '2N1W_0001', '2VRR_2_mod'),     # codes of the templates
              sequence = 'MZF1_tail_pS8_pS111_2N1W_0001')               # code of the target
a.starting_model= 1                 # index of the first model
a.ending_model  = 10                 # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual comparative modeling

