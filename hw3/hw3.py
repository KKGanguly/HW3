import random
from time import time
import sys
sys.path.append("../ezr_24Aug14")
import stats
import ezr as ezr
from ezr import DATA, SETTINGS, csv, medianSd
from stats import SOME, report

class experiment:
    def guess(self, N, d):
        # Pick N rows at random
        some = random.choices(d.rows, k=N)
        # Sort them based on Chebyshev distance
        sorted_rows = d.clone().adds(some).chebyshevs().rows
        return sorted_rows
    def randvsezr(self):
        results = []
        repeats= 20
        #print(the.train,  flush=True, file=sys.stderr)
        print("\n"+the.train)
        d = DATA().adds(csv(the.train))
        b4 = sorted([d.chebyshev(row) for row in d.rows])
        asIs,div = medianSd(b4)
        print(f"asIs\t: {asIs:.3f}")
        print(f"div\t: {div:.3f}")
        print(f"rows\t: {len(d.rows)}")
        print(f"xcols\t: {len(d.cols.x)}")
        print(f"ycols\t: {len(d.cols.y)}\n")
        somes = [stats.SOME(b4,f"asIs,{len(d.rows)}")]
        
        for N in (20, 30, 40, 50):
            d = DATA().adds(csv(the.train))
            
            # Dumb strategy
            start = time()
            dumb = [self.guess(N, d) for _ in range(repeats)]
            dumb = [d.chebyshev(lst[0]) for lst in dumb]
            print(f"dumb,{N}: {(time() - start)/repeats:.2f} secs")
            # Smart strategy
            start = time()
            smart = [d.shuffle().activeLearning() for _ in range(repeats)]
            smart = [d.chebyshev(lst[0]) for lst in smart]
            print(f"smart,{N}: {(time() - start)/repeats:.2f} secs")
            # Append results for each N 
            somes +=   [SOME(dumb,    f"dumb,{N}"),
                    SOME(smart,    f"smart,{N}")]

        report(somes, 0.01)

# Example usage
the = SETTINGS(ezr.__doc__)
experiment = experiment()
if __name__ == "__main__" and len(sys.argv)> 1:
  the.cli()
  random.seed(the.seed)
  getattr(experiment, the.eg, lambda : print(f"ezr: [{the.eg}] unknown."))()