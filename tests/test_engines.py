import unittest
from frontierforge.quantum import qaoa_maxcut
from frontierforge.neuromorphic import lif_run, detect_bursts
from frontierforge.bayes import failure_risk
class EnginesTest(unittest.TestCase):
 def test_quantum(self):
  r=qaoa_maxcut(3,[(0,1),(1,2)],angle_steps=3); self.assertGreaterEqual(r['expected_cut'],0); self.assertLessEqual(r['expected_cut'],2)
 def test_lif(self): self.assertGreater(lif_run([0,2,0])['spike_count'],0)
 def test_burst(self): self.assertGreater(detect_bursts([1,1,1,0],3,3)['windows'],0)
 def test_bayes(self): self.assertGreater(failure_risk(2,20)['posterior_mean_failure_rate'],0)
if __name__=='__main__': unittest.main()
