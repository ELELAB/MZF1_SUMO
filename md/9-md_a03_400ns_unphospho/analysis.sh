make_ndx -f sim.tpr -o protein.ndx << eof
keep 1 
q
eof
trjconv -f traj.xtc -s sim.tpr -pbc mol -ur compact -o traj.mol.ur.xtc << eof
1
eof
trjconv -f traj.mol.ur.xtc -s sim.tpr -pbc nojump -n protein.ndx -o traj.mol.ur.nojump.xtc
rm traj.mol.ur.xtc
tpbconv -s sim.tpr -n protein.ndx -o sim_prot.tpr
g_rms -f traj.mol.ur.nojump.xtc -s sim_prot.tpr -o rmsd.xvg << eof
5
5
eof
g_gyrate -f traj.mol.ur.nojump.xtc -s sim_prot.tpr -o gyrate.xvg << eof
1
eof
trjconv -f traj.mol.ur.nojump.xtc -s sim_prot.tpr -fit rot+trans -dt 200 -n protein.ndx -o movie.dt1000.pdb
mkdir snaps g_chi
cd snaps
trjconv -f ../traj.mol.ur.nojump.xtc -s ../sim_prot.tpr -fit rot+trans -dt 200 -sep -n ../protein.ndx -o model.pdb 
cd ../g_chi
g_chi -f ../traj.mol.ur.nojump.xtc -s ../sim_prot.tpr -g -all -maxchi 4 


