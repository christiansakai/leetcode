from typing import Dict, List

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        if len(pid) != len(ppid):
            return 0
        
        ppid_to_pids = self.construct_map(pid, ppid)
        print(ppid_to_pids)
        
        killed = [] 
        queue = [kill]
        
        while len(queue) > 0:
            qlen = len(queue)
            for i in range(qlen):
                pid = queue.pop(0)
                killed.append(pid)
                
                if pid in ppid_to_pids:
                    children = ppid_to_pids[pid]
                    
                    for c in children:
                        queue.append(c)
                    
        return killed
    
    
    def construct_map(self, pid: List[int], ppid: List[int]) -> Dict[int, List[int]]:
        ppid_to_pids = {}
        for el in ppid:
            ppid_to_pids[el] = []
            
        for i in range(len(pid)):
            _pid = pid[i]
            _ppid = ppid[i]
            
            ppid_to_pids[_ppid].append(_pid)
            
        return ppid_to_pids
