module FIFO(
output reg [7:0] led,
output reg txflag,
input [7:0] rxdata,
input abutton,bbutton,funct,rxflag,txzero,
input reset);
reg [7:0]a;
reg [7:0]b;
reg [7:0]operation;

always @ (reset or abutton or bbutton or funct or txzero)
begin
	if(reset) begin
		a=0;b=0;operation=0;
		txflag=0;
	end
	else 
	begin
		if(abutton && rxflag)
		begin 
			a=rxdata;
		end
		if(bbutton && rxflag)
		begin
			b=rxdata;
		end
		if(funct && rxflag)
		begin
			operation=rxdata;
		end
		if(txzero)
		begin
			txflag=0;
		end
		if(operation == 32)
		begin
			led=a+b;txflag=1;
		end
		else if(operation == 37)
		begin
			led=a|b;txflag=1;
		end
		else if(operation == 36)
		begin
			led=a&b;txflag=1;
		end
		else if(operation == 1)
		begin
			led=a<<b;txflag=1;
		end
		else if(operation == 42)
		begin
			led=(a<b?1:0);txflag=1;
		end		
		else if(operation == 3)
		begin
			led[4:0]=a>>>b;txflag=1;
		end	
		else if(operation == 2)
		begin
			led=a>>b;txflag=1;
		end
		else if(operation == 34)
		begin
			led[4:0]=a-b;txflag=1;
		end
		else if(operation == 38)
		be2	gin
			led=a^b;txflag=1;
		end
		else if(operation == 39)
		begin
			led[4:0]=~(a|b);txflag=1;
		end
		else led=8'b00000000;
		end
end
endmodule
