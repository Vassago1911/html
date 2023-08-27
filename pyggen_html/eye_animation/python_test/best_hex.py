import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
def get_total_error_per_radius()->np.array:
    def _x(cx)->float:
        return np.round(cx.real,2)
    def _y(cx)->float:
        return np.round(cx.imag,2)
    def eq(cx,cy)->bool:
        return abs(cx-cy)<1e-2
    def int_error(cx)->float:
        err_x = abs(_x(cx) - int(_x(cx)))
        err_y = abs(_y(cx) - int(_y(cx)))
        return err_x+err_y        
    zeta_6 = np.exp(2*1j*np.pi*(1/6))
    assert eq(zeta_6**6,1), "zeta_6 not a 6th root of unity, not good"
    standard_hex = np.array([ zeta_6**i for i in range(1,7) ])
    radius_candidates = np.linspace(1,513,65512)
    result = dict()
    min_error = 5000;
    for r in radius_candidates:
        cur_err = sum(map(int_error,r*standard_hex))        
        if cur_err < min_error:
            min_error = cur_err
        result[r] = min_error
    r = pd.Series(result)
    r.plot()
    plt.show();
    return result    
if __name__=="__main__":
    get_total_error_per_radius()    