# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 22:54:47 2022

@author: Lenovo
"""

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

def generate_state():
    return "............................0.................................."

def evolve(stato,bc,n):
    evoluto=[''] * n
    
    if bc=='const':
        status=''.join(('.',stato,'.')) #constant boundaries
    elif bc=='refl':
        status=''.join((stato[0],stato,stato[n-1]))#reflective boundaries
    elif bc=='period':
        status=''.join((stato[n-1],stato,stato[0]))#periodic boundaries
    else: 
        print('Invalid BCs')
        
    for i in range(0,n):
        for j in rule110:
            if status[i:i+3]==j:
                evoluto[i]=rule30[j]
    new_state=''.join((evoluto))
    
    return new_state

def simulation(nsteps,bc,n):
    initial_state = generate_state()
    states_seq = [initial_state]
    print(initial_state)
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state,bc,n)
        print(new_state)
        states_seq.append(new_state)
    return states_seq

bc='period'
states_seq=simulation(100,bc,63)
#print(states_seq)

########################################################

def test_generation_valid_state():
    state = generate_state()
    assert set(state) == {'.', '0'}
    

def test_generation_single_alive():
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1
    
def test_evolution_valid_state():
    for state in states_seq:
        assert set(state) == {'.', '0'}
        
def test_evolution_valid_length():
    for state in states_seq:
        assert len(state)==len(generate_state())

def test_valid_bcs():
    assert bc in ['const','refl','period']
    
#########################################################


