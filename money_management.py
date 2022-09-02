

import numpy as np 


def kelly(expected_return,risk_free_rate,annualized_volatility):
    numerator = expected_return - risk_free_rate
    k = numerator/annualized_volatility**2
    return k

def expected_bankroll_based_on_size(initial_bank_roll,number_of_bets,probability_of_win,probability_of_loss,kelly_ratio):
    win = 1 + (probability_of_win)*np.log(1+kelly_ratio)
    loss = probability_of_loss * np.log(1-kelly_ratio)
    expected_final_bank_roll = initial_bank_roll(win+loss)**number_of_bets
    return expected_final_bank_roll

def growth_ratio(fraction_of_kelly,annualized_volatility,expected_return):
    first_term = fraction_of_kelly - (fraction_of_kelly**2 / 2)
    second_term = expected_return**2 / annualized_volatility**2
    gr = first_term*second_term
    return gr 


def probability_of_reaching_A_before_B(fraction_of_kelly,A,B):
    numerator = 1 - A**(1-(2/fraction_of_kelly))
    denominator = B**(1-(2/fraction_of_kelly)) - A**(1-(2/fraction_of_kelly))
    p = numerator/denominator
    return p 

def expected_time_to_beat_other_strategies(annualized_volatility,fraction_of_kelly,outperform_percentage):
    first_term = (2/(annualized_volatility**2 *(1-fraction_of_kelly)**2))
    second_term = np.log(1+outperform_percentage)
    time_to_outperform = first_term*second_term
    return time_to_outperform
