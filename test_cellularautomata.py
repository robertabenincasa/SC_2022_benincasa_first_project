from random import seed
from random import randint

""" The following dictionaries provide Wolfram's rules of cellular evolution. 
The 0 indicates an alive cell, whereas the dot represent a dead one."""

rule30 = {"000": '.',
          "00.": '.',
          "0.0": '.',
          "...": '.',
          "0..": '0',
          ".00": '0',
          ".0.": '0',
          "..0": '0',
         }
rule90 = {"000": '.',
          "00.": '0',
          "0.0": '.',
          "...": '.',
          "0..": '0',
          ".00": '0',
          ".0.": '.',
          "..0": '0',
         }
rule110 = {"000": '.',
          "00.": '0',
          "0.0": '0',
          "...": '.',
          "0..": '.',
          ".00": '0',
          ".0.": '0',
          "..0": '0',
         }
rule184 = {"000": '0',
          "00.": '.',
          "0.0": '0',
          "...": '.',
          "0..": '0',
          ".00": '0',
          ".0.": '.',
          "..0": '.',
         }
""" The following parameters define the rule, the boundary conditions,
the number of elements in the strings and the number of steps, respectively. They need to be fixed. """

rule=rule30
bc='period'
n=12
nsteps=10

seed(7)
def generate_state():
    "This function generates the initial state as a string having n elements composed of "
    "The random function is used in order to have the 0 in a random position."
    "If one wants to maintain the same position than the seed must be fixed above."
    state = ['.']*(n-1)
    state.insert(randint(0,n-1),'0')
    initial_state=''.join(state)
    return initial_state

def boundcond(stato):
    """This function applies the boundary conditions that one chooses to adopt.
    The boundaries can be reflective, periodic or constant. 
    It takes as input the state to be evolved. """
    if bc=='const':
        status=''.join(('.',stato,'.')) #constant boundaries
    elif bc=='refl':
        status=''.join((stato[0],stato,stato[n-1]))#reflective boundaries
    elif bc=='period':
        status=''.join((stato[n-1],stato,stato[0]))#periodic boundaries
    else: 
        print('Invalid BCs')
    return status

def evolve(stato):
    """ This function perfoms the evolution of each state following the chosen rule.

    The rule can be rule 30, 90, 110 or 184. 
    It takes as input the state to be evolved. """

    evoluto=[''] * n
    status=boundcond(stato)
#the evolution is performed following the chosen rule      
    for i in range(0,n):
        for j in rule:
            if status[i:i+3]==j:
                evoluto[i]=rule[j]
    new_state=''.join((evoluto))
    
    return new_state

def simulation(nsteps):
    """ This function performs the simulation by evolving the system from the initial state for nsteps."""
    initial_state = generate_state()
    states_seq = [initial_state]
    print(initial_state)
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state)
        print(new_state)
        states_seq.append(new_state)
    return states_seq

states_seq=simulation(nsteps)


########################################################

def test_generation_valid_state():
    """ This function tests that the initial state is valid.

    GIVEN: the initial state from generate.state()
    THEN: it results in a string composed of . and 0. """
    state = generate_state()
    assert set(state) == {'.', '0'}
    

def test_generation_single_alive():
    """ This function tests if the initial state is a string composed of . and only one 0.
    GIVEN: the initial state from generate.state()
    THEN: it produces a string formed of . and only one 0.""" 
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1
    
def test_evolution_valid_state():
    """ This function tests that the evolve function returns valid states when used.
    
    GIVEN: a valid state of my simulation
    WHEN: I apply to it the evolve function
    THEN: the resulting state is still a valid one
    """
    for state in states_seq:
        assert set(state) == {'.', '0'}
        
def test_evolution_valid_length():
    """ This function tests that the evolve function returns a state of the same length of the initial one.
    
    GIVEN: a valid state of my simulation
    WHEN: I apply to it the evolve function
    THEN: the resulting state has the same length of the initial one from generate.state().
    """          
    for state in states_seq:
        assert len(state)==len(generate_state())

def test_valid_bcs():
    """ This function tests that the selected boundary conditions are correct.
    
    GIVEN: a string for the value of the boundary conditions
    THEN: it must be one among the following.
    """         
    assert bc in ['const','refl','period']
    
#########################################################
