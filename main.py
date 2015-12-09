from tm import *
import sys

def createMachine():

	f = open(sys.argv[1], "r")

	nStates, nTransitions = map(int, f.readline().strip().split())
	machine = TuringMachine()

	#reading states
	for i in range (0, nStates):
		line = f.readline().strip().split()
		value = line[0]
		state = State(value)
		machine.addState(state)

	#reading transitions
	for i in range (0, nTransitions):
		line = f.readline().strip().split()
		source = line[0]
		destination = line[1]
		read = line[2]
		write = line[3]
		direction = Transition.Direction.RIGHT if line[4] == 'R' else Transition.Direction.LEFT
		transition = Transition(read, write, machine.getState(destination), direction)
		machine.addTransition(source, transition)

	#read initial state
	initialState = f.readline().strip()
	machine.setInitState(initialState)

	return machine

def readTape():
	f = open(sys.argv[2], "r")

	string = f.readline().strip()
	tape = Tape(string)

	return tape

if __name__ == "__main__":
    #read file and create the machine
    machine = createMachine()
    #read tape
    tape = readTape()
    machine.setTape(tape)
    #simulate
    machine.simulate()

    print(tape.cells)
