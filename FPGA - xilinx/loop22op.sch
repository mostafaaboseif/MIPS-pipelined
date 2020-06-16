<?xml version="1.0" encoding="UTF-8"?>
<drawing version="7">
    <attr value="zynq" name="DeviceFamilyName">
        <trait delete="all:0" />
        <trait editname="all:0" />
        <trait edittrait="all:0" />
    </attr>
    <netlist>
        <signal name="abutton" />
        <signal name="bbutton" />
        <signal name="clk" />
        <signal name="RxD" />
        <signal name="XLXN_10" />
        <signal name="XLXN_11(7:0)" />
        <signal name="led(7:0)" />
        <signal name="funct" />
        <signal name="reset" />
        <signal name="XLXN_32" />
        <signal name="TxD" />
        <signal name="XLXN_33" />
        <signal name="XLXN_24" />
        <signal name="XLXN_23" />
        <signal name="txzero" />
        <port polarity="Input" name="abutton" />
        <port polarity="Input" name="bbutton" />
        <port polarity="Input" name="clk" />
        <port polarity="Input" name="RxD" />
        <port polarity="Output" name="led(7:0)" />
        <port polarity="Input" name="funct" />
        <port polarity="Input" name="reset" />
        <port polarity="Output" name="TxD" />
        <port polarity="Input" name="txzero" />
        <blockdef name="async_transmitter">
            <timestamp>2019-11-13T14:32:39</timestamp>
            <rect width="256" x="64" y="-192" height="192" />
            <line x2="0" y1="-160" y2="-160" x1="64" />
            <line x2="0" y1="-96" y2="-96" x1="64" />
            <rect width="64" x="0" y="-44" height="24" />
            <line x2="0" y1="-32" y2="-32" x1="64" />
            <line x2="384" y1="-160" y2="-160" x1="320" />
            <line x2="384" y1="-32" y2="-32" x1="320" />
        </blockdef>
        <blockdef name="async_receiver">
            <timestamp>2019-11-13T14:49:54</timestamp>
            <rect width="256" x="64" y="-256" height="256" />
            <line x2="0" y1="-224" y2="-224" x1="64" />
            <line x2="0" y1="-32" y2="-32" x1="64" />
            <line x2="384" y1="-224" y2="-224" x1="320" />
            <line x2="384" y1="-160" y2="-160" x1="320" />
            <line x2="384" y1="-96" y2="-96" x1="320" />
            <rect width="64" x="320" y="-44" height="24" />
            <line x2="384" y1="-32" y2="-32" x1="320" />
        </blockdef>
        <blockdef name="FIFO">
            <timestamp>2019-11-14T11:41:2</timestamp>
            <line x2="0" y1="160" y2="160" x1="64" />
            <line x2="0" y1="96" y2="96" x1="64" />
            <line x2="0" y1="32" y2="32" x1="64" />
            <line x2="0" y1="-96" y2="-96" x1="64" />
            <rect width="64" x="0" y="-44" height="24" />
            <line x2="0" y1="-32" y2="-32" x1="64" />
            <rect width="64" x="320" y="-44" height="24" />
            <line x2="384" y1="-32" y2="-32" x1="320" />
            <line x2="0" y1="-224" y2="-224" x1="64" />
            <line x2="0" y1="-160" y2="-160" x1="64" />
            <line x2="384" y1="-224" y2="-224" x1="320" />
            <rect width="256" x="64" y="-252" height="444" />
        </blockdef>
        <blockdef name="vcc">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-32" y2="-64" x1="64" />
            <line x2="64" y1="0" y2="-32" x1="64" />
            <line x2="32" y1="-64" y2="-64" x1="96" />
        </blockdef>
        <blockdef name="copy_of_fdc">
            <timestamp>2019-11-14T11:30:20</timestamp>
            <rect width="116" x="64" y="-168" height="104" />
            <line x2="144" y1="-64" y2="-32" x1="144" />
            <line x2="64" y1="-96" y2="-96" x1="0" />
            <line x2="80" y1="-80" y2="-96" x1="64" />
            <line x2="64" y1="-96" y2="-112" x1="80" />
            <line x2="64" y1="-144" y2="-144" x1="0" />
            <line x2="176" y1="-128" y2="-128" x1="240" />
        </blockdef>
        <block symbolname="async_receiver" name="XLXI_3">
            <blockpin signalname="clk" name="clk" />
            <blockpin signalname="RxD" name="RxD" />
            <blockpin signalname="XLXN_10" name="RxD_data_ready" />
            <blockpin name="RxD_idle" />
            <blockpin name="RxD_endofpacket" />
            <blockpin signalname="XLXN_11(7:0)" name="RxD_data(7:0)" />
        </block>
        <block symbolname="FIFO" name="XLXI_6">
            <blockpin signalname="abutton" name="abutton" />
            <blockpin signalname="bbutton" name="bbutton" />
            <blockpin signalname="funct" name="funct" />
            <blockpin signalname="XLXN_10" name="rxflag" />
            <blockpin signalname="reset" name="reset" />
            <blockpin signalname="XLXN_11(7:0)" name="rxdata(7:0)" />
            <blockpin signalname="XLXN_32" name="txflag" />
            <blockpin signalname="led(7:0)" name="led(7:0)" />
            <blockpin signalname="txzero" name="txzero" />
        </block>
        <block symbolname="vcc" name="XLXI_11">
            <blockpin signalname="XLXN_24" name="P" />
        </block>
        <block symbolname="copy_of_fdc" name="XLXI_12">
            <blockpin signalname="XLXN_33" name="CLR" />
            <blockpin signalname="XLXN_32" name="C" />
            <blockpin signalname="XLXN_24" name="D" />
            <blockpin signalname="XLXN_23" name="Q" />
        </block>
        <block symbolname="async_transmitter" name="XLXI_1">
            <blockpin signalname="clk" name="clk" />
            <blockpin signalname="XLXN_23" name="TxD_start" />
            <blockpin signalname="led(7:0)" name="TxD_data(7:0)" />
            <blockpin signalname="TxD" name="TxD" />
            <blockpin signalname="XLXN_33" name="TxD_busy" />
        </block>
    </netlist>
    <sheet sheetnum="1" width="7040" height="5440">
        <instance x="2400" y="1536" name="XLXI_3" orien="R0">
        </instance>
        <branch name="abutton">
            <wire x2="3056" y1="1264" y2="1264" x1="3024" />
        </branch>
        <iomarker fontsize="28" x="3024" y="1264" name="abutton" orien="R180" />
        <branch name="bbutton">
            <wire x2="3056" y1="1328" y2="1328" x1="3024" />
        </branch>
        <iomarker fontsize="28" x="3024" y="1328" name="bbutton" orien="R180" />
        <branch name="RxD">
            <wire x2="2400" y1="1504" y2="1504" x1="2368" />
        </branch>
        <iomarker fontsize="28" x="2368" y="1504" name="RxD" orien="R180" />
        <branch name="XLXN_10">
            <wire x2="2864" y1="1312" y2="1312" x1="2784" />
            <wire x2="2864" y1="1312" y2="1584" x1="2864" />
            <wire x2="3056" y1="1584" y2="1584" x1="2864" />
        </branch>
        <branch name="XLXN_11(7:0)">
            <wire x2="2800" y1="1504" y2="1504" x1="2784" />
            <wire x2="3056" y1="1456" y2="1456" x1="2800" />
            <wire x2="2800" y1="1456" y2="1504" x1="2800" />
        </branch>
        <branch name="led(7:0)">
            <wire x2="3488" y1="1456" y2="1456" x1="3440" />
            <wire x2="3488" y1="1456" y2="1584" x1="3488" />
            <wire x2="3504" y1="1584" y2="1584" x1="3488" />
            <wire x2="3856" y1="1392" y2="1392" x1="3488" />
            <wire x2="3488" y1="1392" y2="1456" x1="3488" />
        </branch>
        <iomarker fontsize="28" x="2272" y="1312" name="clk" orien="R180" />
        <branch name="funct">
            <wire x2="3056" y1="1520" y2="1520" x1="3024" />
        </branch>
        <branch name="reset">
            <wire x2="3056" y1="1392" y2="1392" x1="3024" />
        </branch>
        <instance x="3056" y="1488" name="XLXI_6" orien="R0">
        </instance>
        <iomarker fontsize="28" x="3024" y="1520" name="funct" orien="R180" />
        <iomarker fontsize="28" x="3024" y="1392" name="reset" orien="R180" />
        <branch name="clk">
            <wire x2="2336" y1="1312" y2="1312" x1="2272" />
            <wire x2="2400" y1="1312" y2="1312" x1="2336" />
            <wire x2="2336" y1="944" y2="1312" x1="2336" />
            <wire x2="3760" y1="944" y2="944" x1="2336" />
            <wire x2="3760" y1="944" y2="1264" x1="3760" />
            <wire x2="3856" y1="1264" y2="1264" x1="3760" />
        </branch>
        <iomarker fontsize="28" x="3504" y="1584" name="led(7:0)" orien="R0" />
        <instance x="3376" y="1088" name="XLXI_11" orien="R0" />
        <instance x="3856" y="1424" name="XLXI_1" orien="R0">
        </instance>
        <branch name="XLXN_24">
            <wire x2="3440" y1="1088" y2="1136" x1="3440" />
            <wire x2="3472" y1="1136" y2="1136" x1="3440" />
        </branch>
        <branch name="XLXN_23">
            <wire x2="3728" y1="1152" y2="1152" x1="3712" />
            <wire x2="3728" y1="1152" y2="1328" x1="3728" />
            <wire x2="3856" y1="1328" y2="1328" x1="3728" />
        </branch>
        <branch name="TxD">
            <wire x2="4256" y1="1264" y2="1264" x1="4240" />
            <wire x2="4304" y1="1264" y2="1264" x1="4256" />
        </branch>
        <instance x="3472" y="1280" name="XLXI_12" orien="R0" />
        <branch name="XLXN_32">
            <wire x2="3456" y1="1264" y2="1264" x1="3440" />
            <wire x2="3472" y1="1184" y2="1184" x1="3456" />
            <wire x2="3456" y1="1184" y2="1264" x1="3456" />
        </branch>
        <branch name="XLXN_33">
            <wire x2="3616" y1="1248" y2="1488" x1="3616" />
            <wire x2="4256" y1="1488" y2="1488" x1="3616" />
            <wire x2="4256" y1="1392" y2="1392" x1="4240" />
            <wire x2="4256" y1="1392" y2="1488" x1="4256" />
        </branch>
        <iomarker fontsize="28" x="4304" y="1264" name="TxD" orien="R0" />
        <branch name="txzero">
            <wire x2="3056" y1="1648" y2="1648" x1="3024" />
        </branch>
        <iomarker fontsize="28" x="3024" y="1648" name="txzero" orien="R180" />
    </sheet>
</drawing>