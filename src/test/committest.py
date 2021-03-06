import unittest
import os
from geogitpy.repo import Repository
import time
from geogitpy import geogit
from geogitpy.commit import Commit

class GeogitCommitTest(unittest.TestCase):
        
    repo = Repository(os.path.join(os.path.dirname(__file__), 'data/testrepo'))

    def getTempPath(self):
        return os.path.join(os.path.dirname(__file__), "temp", str(time.time())).replace('\\', '/')

    def getClonedRepo(self):
        dst = self.getTempPath()
        return self.repo.clone(dst) 
    
    def testFromRef(self):
        ref = self.repo.head.ref
        commit = Commit.fromref(self.repo, ref)
        log = self.repo.log()
        headcommit = log[0]
        self.assertEqual(headcommit.ref, commit.ref)
        self.assertEqual(headcommit.committerdate, commit.committerdate)        
        
    def testCommitDiff(self):
        log = self.repo.log()
        commit = log[0]        
        diff = commit.diff()
        self.assertEquals(1, len(diff))
        self.assertEquals("parks/5", diff[0].path)        