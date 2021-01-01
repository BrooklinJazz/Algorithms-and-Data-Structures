# Overview and Introduction to Lisp
## What is Computer Science	
- computer science is not about computers nor is it a science
- coding and magic have more in common
- cs is actually about "process"
- declarative vs imperative (how to) knowledge
- exploit the rules to be a master programmer
- in computer science we are in the business of formalizing imperative knowledge
- the only reason it's possible for us to work on large scale programs (that we cannot possibly fit in our head) is because there are techniques that allow us to

## Techniques for Controlling Complexity
- computer science deals with idealised components
- not a big difference between what you can build and what you can imagine
- the constraints composed in building large software systems are the limitations of our own minds


what are the techniques?
1. Abstraction "Black Box Abstraction"
visualizing input -> process -> output without going into the detail of process
black box abstraction (put things in a box) so we can build bigger boxes
	- Primitive Objects
		- Primitive Procedures
		- Primitive Data
  - Means of Combination 
	- Means of Abstraction
	- Capturing Common Patterns

line between data vs procedures is going to blur	

2. Conventional Interface
- Generic Operations
- Large Scale Structure and Modularity
- Object Oriented Programming
- Operation on Aggregates

we're going to express in lisp the process of interpreting lisp

3. Metaliguistic Abstraction

## Thinking About a Language
- Primitive Elements (+ 3 3.2 2.9)
	- operator +
	- operand 4
	- combination (+ 4 2)
- Means of Combination
- Means of Abstraction

Prefix Notation

thinking of combinations as a tree

- +
- 3
- - *
- - 5
- - 6
- 8
- 2

parenthesis are just a way to write the above 3 dimensional structure as a linear character string

using bracket highlighting or indentation to help us track parenthesis

the power is in the ability to name the idea of something such as `square`

syntactic sugar
- (define (square x)(* x x))
- (define square (lambda (x) (* x x)))


## Procedures and the processes they generate
- linear iterative process
	- does not grow and shrink, or create deferred operations
	- summarized by having a fixed number of state variables
	- can be resumed at any point
	- Scheme can execute linear iterative process in constant time, but
	languages like Ada, Pascal, C consume memory growing with the number of procedure calls (resorting to special purpose looping constructs: for, while, do, repeat, until)
	
- linear recursive process
	- expansion: builds up a chain of deferred operations
	- contraction: as deferred operations are performed
	- requires that the interpreter keep track of the operations to be performed later on
	- the length of the chain grows proportional to big O notation
	- for example a On operations grows at a rate of n so it is a linear recursive process
	- hidden information maintained by the interpreter

# 2.1 Representing Rational Numbers
- cons
	- car
	- cdr	

# 1.B Procedures and Processes; Substitution Model.
- shapes of processes
- iterative
	- time = O(x)
	- space = O(1)
- vs recursive
- time vs space complexity

# Representing Sequences
- closure property of cons: the ability to create pairs whose elements are pairs
- trees and other data types can be represented by using the closure property of cons:

## Test Questions
1. what is the diff between declarative and imperative knowledge
2. Define linear iterative process and linear recursive process

cons(a,b) => (a, b)
cons(c, cons(a,b)) => (c, (a,b))
car (c,(a,b)) => c
cdr (c, (a,b)) => (a,b)
((a,b), (c,d))


