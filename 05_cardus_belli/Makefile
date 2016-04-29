all:
	python solution.py < input1.txt > myoutput1.txt
	@diff myoutput1.txt output1.txt
	python solution.py < input2.txt > myoutput2.txt
	@diff myoutput2.txt output2.txt
	python solution.py < input3.txt > myoutput3.txt
	@diff myoutput3.txt output3.txt
clean:
	rm -rf myoutput1.txt myoutput2.txt myoutput3.txt
