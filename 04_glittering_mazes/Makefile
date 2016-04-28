all:
	python solution.py < sample_input.txt > mysample_output.txt
	@diff mysample_output.txt sample_output.txt
	python solution.py < sample_input2.txt > mysample_output2.txt
	@diff mysample_output2.txt sample_output2.txt
#	python solution.py < input1.txt > myoutput1.txt
#	@diff myoutput1.txt output1.txt
#	python solution.py < input2.txt > myoutput2.txt
#	@diff myoutput2.txt output2.txt
clean:
	rm -rf myoutput1.txt myoutput2.txt mysample_output.txt mysample_output2.txt
