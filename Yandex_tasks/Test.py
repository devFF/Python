def create_pref_sum(seq):
    pref_list = [0]
    for i in range(1,len(seq)+1):
        if seq[i-1] == 0:
            pref_list.append(pref_list[i-1]+1)
        else:
            pref_list.append(pref_list[i-1])
    return pref_list
    
class FindZeroesNumber:
    def __init__(self, seq):
        self.pref_list = create_pref_sum(seq)
        
    def calc_zeroes(self,L,R):
        return self.pref_list[R] - self.pref_list[L]
        

if __name__ == '__main__':
    obj = FindZeroesNumber(seq=[0,1,2,3,0,0,0,4,0,3,2,0,1,0,0])
    print(obj.calc_zeroes(0,15))