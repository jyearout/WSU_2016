####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'DizzyD' #'The name the team gives to itself'  Only 10 chars displayed.
strategy_name = 'Naive belief in humanity'  #'The name the team gives to this strategy'
strategy_description = 'Work towards co-op, but defect away if score becomes too unfavorable'    #'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    move_for_round = ''
    vindictive = 0
    v_count = 4
#opp_is_alt = 0
    min_dmg = 0
    if(len(my_history) < 4):
	move_for_round = 'c'
    elif(their_history == 'bbb'):
	vindictive = 1
    elif(vindictive >= 1): #has there been too much defection from their side?
	move_for_round = 'b'
	v_count -= 1
	if(v_count <= 0):
		vindictive = 0
    elif (opp_is_alt(their_history) == 1):
	if (their_history[-1] == 'c'):
	    move_for_round = 'b'
	else:
	    move_for_round = 'c'
    elif (min_damage(my_score, their_score) == 1):
        move_for_round = 'b'
    if move_for_round == '':
        move_for_round = 'c'
    return move_for_round


def opp_is_alt(history):
    
    alt = 0
    switcher = 1
    still_possible = 1
    if (history[0] == 'c'):
	for hist in history:
            if(switcher % 2 == 1):
                if (history[switcher - 1] != 'c'):
                    still_possible = 0
            else:
                if (history[switcher - 1] != 'b'):
                    still_possible = 0
            switcher += 1 
    else:
	for hist in history:
	    if(switcher % 2 == 1):
	        if (history[switcher - 1] != 'b'):
	            still_possible = 0
	    else:
	        if (history[switcher - 1] != 'c'):
	            print history[switcher - 1] + ' =c'
	            still_possible = 0
	    switcher += 1 
    if (still_possible == 1):
        return 1
    else:
	return 0
	
def min_damage(m_score, t_score):
    minimizing = 0
    if(m_score < t_score) and (m_score - t_score <= -2200):
        minimizing = 1
        return 1
    elif minimizing == 1:
        if m_score - t_score >= -500:
            minimizing = 0
            return 0
        else:
            return 1
    else:
        return 0
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: collude on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
        print ''
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='c')             