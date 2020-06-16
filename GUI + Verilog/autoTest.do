vsim work.atb_all
mem load -format binary -infile instructionMem.txt /atb_all/aa/Imemory
mem load -format binary -infile regFile.txt /atb_all/bb/Rf
mem load -format binary -infile dataMem.txt /atb_all/dd/Dmemory
run 200
mem save -format binary -outfile regFile.txt -wordsperline 1 /atb_all/bb/Rf
mem save -format binary -outfile dataMem.txt -wordsperline 1 /atb_all/dd/Dmemory
quit
