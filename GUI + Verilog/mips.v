//////////////////////////////////////////////////////////////////////////////////
// 
// Project: MIPS Processor
// Create Date:   11/10/2019
// 
// Description: 32-bit processor to execute machine code, supplemented by an assembler,
//		a user interface and an automated testing architecture
//
// Team Members: Mostafa Amgad - Mahmoud Osama - Mariam AbdelRahman
//	   	 Mohamed Abdullah - Mostafa Sedik	
// 
// Delivered to: M.Ahmed Fathy
// Delivery Date: 15/11/2019
//
//////////////////////////////////////////////////////////////////////////////////

//             ****************Memories****************
module registerFile(readReg1,readReg2,writeReg,writeData,regWrite,readData1,readData2,clk);
input[4:0] readReg1,readReg2,writeReg;  //address to read(rs,rt) or write(rd) data in regsiter file
input [31:0] writeData;  //the data to be written in the register file
input regWrite;  //control signal to enable writing in register 
input clk;
output [31:0] readData1,readData2;  //the data read from regsiter file
reg[31:0] Rf[0:31];	//2D array where we save the contents of register file
assign readData1 = Rf[readReg1];   //we read data at a specific address from register file
assign readData2 = Rf[readReg2];
always@(posedge clk)
begin
 if (regWrite)Rf[writeReg] <= writeData;   //if the control signal for write is set, we write in a specific address in register file
end
endmodule

module iMem (instruction,pc,clk);
input [31:0] pc;  //the program counter to select instructions form instruction memory
input clk;
output reg [31:0] instruction;  //the instruction which will be executed at this cycle
reg [31:0] Imemory[0:31];  //2D array where we load the contents of instruction memory
always @(posedge clk)
begin
instruction <= Imemory[pc];  //select instruction at a specific pc
end
endmodule

module dMem(address,memRead,memWrite,writeData,readData,clk);
input [31:0] address ; //address to read or write data from memory in lw,sw instructions
input memRead,memWrite;  //control signals to enable reading or writing in memory
input [31:0] writeData;  //data to be written in data memory
output reg [31:0] readData;  //data read from memory from specific address
reg [31:0] Dmemory[0:31];  //2D array where we save the contents of memory file
input clk;
always @(negedge clk)
begin
if(memRead==1 && memWrite==0)
readData<=Dmemory[address];   //when we aren't writing in the data memory, memWrite must be disabled
else if(memRead==0 && memWrite==1)
begin
Dmemory[address] <= writeData;  //write data in the 2D array at a specific address
readData<=32'hzzzzzzzz;    //when data is not read from data memory, it's set to high impedance
end
else if(memRead==0&&memWrite==0)
readData <= 32'hzzzzzzzz;
else 
readData<=32'hxxxxxxxx;   
end
endmodule

//             ****************Control****************
module controlUnit (op,regDst,branch,bne,memRead,memtoReg,aluOp,memWrite,aluSrc,regWrite,jump,raMux);
// a module that takes the op code as input and returns the control signals to control the other modules behavior 
input [5:0] op ;  //input to control unit 
output reg regDst,branch,memRead,memtoReg,memWrite,aluSrc,regWrite,jump,bne,raMux; 
output reg [1:0] aluOp;
// the output changes whenever the op code changes ( combinational circuit)
always @(op)
begin
case(op)
0:{regDst,aluSrc,memtoReg,regWrite,memRead,memWrite,branch,bne,aluOp,jump,raMux}<=12'b100100001000;//R-format
35:{regDst,aluSrc,memtoReg,regWrite,memRead,memWrite,branch,bne,aluOp,jump,raMux}<=12'b011110000000;//lw
43:{regDst,aluSrc,memtoReg,regWrite,memRead,memWrite,branch,bne,aluOp,jump,raMux}<=12'bx1x001000000;//sw
4:{regDst,aluSrc,memtoReg,regWrite,memRead,memWrite,branch,bne,aluOp,jump,raMux}<=12'bx0x000100100;//beq
5:{regDst,aluSrc,memtoReg,regWrite,memRead,memWrite,branch,bne,aluOp,jump,raMux}<=12'bx0x000010100;//bne
2:{regDst,aluSrc,memtoReg,regWrite,memRead,memWrite,branch,bne,aluOp,jump,raMux}<=12'bxxx000xxxx10;//j
8:{regDst,aluSrc,memtoReg,regWrite,memRead,memWrite,branch,bne,aluOp,jump,raMux}<=12'b010100000000;//addi
13:{regDst,aluSrc,memtoReg,regWrite,memRead,memWrite,branch,bne,aluOp,jump,raMux}<=12'b010100001100;//ori
3:{regDst,aluSrc,memtoReg,regWrite,memRead,memWrite,branch,bne,aluOp,jump,raMux}<=12'bxxx100xxxx11;//jal
63:{regDst,aluSrc,memtoReg,regWrite,memRead,memWrite,branch,bne,aluOp,jump,raMux}<=12'bxxxxxxxxxxxx;//save
endcase
end
endmodule

module aluControl (aluOp,funct,aluFn,jr);
//a module to specify the operation which the alu will excute
input [1:0] aluOp;
input [5:0] funct;
output reg [3:0] aluFn;
output  reg jr ;
//input clk;
// outout changes with changes in aluOP or function in case of R-type Instructions
always@(aluOp,funct)
begin
if(aluOp==0)begin aluFn<=4'b0010  ; jr<=0; end
else if(aluOp==1) begin aluFn<=4'b0110; jr<=0; end 
else if(aluOp==3) begin aluFn<=4'b0001; jr<=0; end
//if the instruction is R-type the alu behavior depends on the Function Field
else if(aluOp==2)//R-format
begin
case(funct)
0:begin aluFn<=14;jr<=0; end //sll
2:begin aluFn<=13;jr<=0; end //srl
3:begin aluFn<=15;jr<=0; end //sra
8:begin aluFn<=4'bxxxx;jr<=1; end //jr
32:begin aluFn<=4'b0010;jr<=0; end //add
34:begin aluFn<=4'b0110;jr<=0; end //sub
36:begin aluFn<=4'b0000;jr<=0; end //and
37:begin aluFn<=4'b0001;jr<=0; end //or
38:begin aluFn<=8;jr<=0; end //xor
39:begin aluFn<=4'b1100;jr<=0; end //nor
42:begin aluFn<=4'b0111;jr<=0; end //slt
endcase
end
else aluFn<=4'bxxxx;
end
endmodule

//    ****************Muxes****************
module mux(sel,A,B,result);
// a simple general purpose mux to select between 2 inputs each 32 bit 
input [31:0] A,B;  //mux inputs
input sel;  //mux selector
output [31:0] result;  //output of mux
assign result = (~sel)?A:(sel)?B:32'hxxxxxxxx;  //if sel=0,output is A
endmodule

module mux5bit(sel,A,B,result);
// a simple general purpose mux to select between 2 inputs each 4 bit 
input [4:0] A,B; //mux inputs
input sel;  //mux selector
output [4:0] result;  //output of mux
assign result = (~sel)?A:(sel)?B:5'bxxxxx;
endmodule

//    ****************Extensions****************
module signExtend(im,imExtended);
//a module that extends a 16 bit data to make it 32 bit and make it usable in MIPS depeding on its sign (MSB)
input wire [15:0] im;  //the 16-bit address taken for I-format insrtuctions
output reg [31:0] imExtended;  //we extend the 16-bit to 32-bit
//the output changes with the change of the 16 bits input
always@ (im)
begin   //if the number is negative, we add ones to the left to keep the sign
if(im[15]==1)
imExtended <= {16'hffff,im}; 
else if(im[15]==0)
imExtended <= {16'h0000,im};
else 
imExtended <= 32'hxxxxxxxx;
end
endmodule

module zeroExtend(im,imExtended);
//a module that extends a 16 bit data to make it 32 bit and make it usable in MIPS (unsigned extension)
input wire [15:0] im;
output [31:0] imExtended;
assign imExtended = {16'h0000,im};  //this module is used for logical operators where we don't need signs
endmodule 


//    ****************ALU****************
module alu(ctrl,a,b,shamt,out,zeroFlag);
// the module which is resposible of doing all the Mathematical and logical operations 
// it takes two operands 32 bit each 
// a 4 bits control signal & shift amount if the operation is shifting
input [3:0] ctrl ;  //control to select operations for ALU
input [31:0] a,b ;  //the 2 input registers to the ALU
input [4:0]shamt;  //shift amount for sll,srl,sra operations
output reg [31:0] out;  //ALU result
output zeroFlag;   //used for branch operations
assign zeroFlag=(a==b?1:0);   //when the 2 registers are equal, we set the flag
// the output changes with the change of the operands or the alu control signal
always@(a,b,ctrl)
case(ctrl) 
0:out<=a&b;  //and
1:out<=a|b;  //or
2:out<=a+b;  //add
6:out<=a-b;  //sub
7:out<=(a<b?1:0);  //stl : when a is less than b , we set the output 
8:out<=a^b;   //xor 
12:out<=~(a|b);  //nor 
13:out<=(a>>shamt);  //srl
14:out<=(a<<shamt);  //sll
15:out<=(a>>>shamt);  //sra
endcase
endmodule 


module atb_all();
integer pc,pcout,file,i;
wire [4:0] writeRegPre,writeReg;
wire [31:0] writeData,writeDataPre;
reg clk;
wire zeroFlag,regDst,aluSrc,memtoReg,regWrite,memWrite,memRead,jump,branch,jr,bne,raMux;
wire [3:0] aluCtrl;
wire [31:0] readData1,readData2,aluResult,writeDataMem,readDataMem;
wire [31:0] imExtended,aluInput2,signExtended,zeroExtended;
wire [31:0] instruction;
wire [15:0] im;
wire [5:0] op,funct;
wire [4:0] rs,rt,rd,shamt;
wire [1:0] aluOp;
wire extendSignal ;
reg [31:0] m,xx;

assign op = instruction [31:26];
assign rs = instruction [25:21];
assign rt = instruction [20:16];
assign rd = instruction [15:11];
assign im = instruction [15:0];
assign shamt = instruction [10:6];
assign funct = instruction [5:0]; 
assign extendSignal=aluOp[0]&&aluOp[1];

iMem aa (instruction,pc,clk);
registerFile bb (rs,rt,writeReg,writeData,(regWrite&&(!jr)),readData1,readData2,clk);
alu cc (aluCtrl,readData1,aluInput2,shamt,aluResult,zeroFlag);
dMem dd (aluResult,memRead,memWrite,readData2,readDataMem,clk);
signExtend ee (im,signExtended);
mux muxAluSrc (aluSrc,readData2,imExtended,aluInput2);
mux muxMemtoReg (memtoReg,aluResult,readDataMem,writeDataPre);
mux5bit muxRegDst (regDst,rt,rd,writeRegPre);
controlUnit ii (op,regDst,branch,bne,memRead,memtoReg,aluOp,memWrite,aluSrc,regWrite,jump,raMux);
aluControl jj (aluOp,funct,aluCtrl,jr);
zeroExtend kk (im,zeroExtended);
mux LL(extendSignal,signExtended,zeroExtended,imExtended);
mux5bit mm(raMux,writeRegPre,5'b11111,writeReg);
mux nn(raMux,writeDataPre,(xx+1),writeData);

initial
begin
pc=-1;
clk=1;
end

always@(posedge clk)
begin
xx<=pc;pc<=pc+1;m<=pc;
end

always@(negedge clk)
begin
if(jr)pc<=readData1;
else if(jump)begin
pc<={pc[31:28],{2'b00},instruction[25:0]};
end
else if((branch&&zeroFlag)||(bne&&!zeroFlag)) pc<=(imExtended+pc);
end

always@(posedge clk)
begin
if(instruction == 32'hffffffff)
begin
file = $fopen ("pc.txt", "w");
$fwrite(file,"%b",m);
end
end

always
begin
#1
clk=~clk;
end

endmodule