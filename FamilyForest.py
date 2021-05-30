class FamilyForest:
    self.family_rep = {}
    def make_family(self, s: str) -> None:
        self.family_rep[s] = [s]
        
    def union(self, s: str, t: str) -> str:
        if s in family_rep and t not in family_rep:
            self.family_rep[s].append(t)
            return s
        if t in family_rep and s not in family_rep:
            self.family_rep[t].append(s)
            return t
        if s in family_rep and t in family_rep:
            self.family_rep[s].append(family_rep[t])
            return s
        else:
            self.family_rep[s] = [s,t]
            return s
               

    def find(self, s: str) -> str:
        for i in self.family_rep:
            if s in self.family_rep[i]:
                return i
        