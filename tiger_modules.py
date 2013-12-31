#!/usr/bin/python

#tiger_modules.py


def getRTZ(fil):

/*			RT="Record Type"
			VERSION="Version Number"
			TLID="TIGER Line ID
			RTSQ="Record Sequence Number"
			ZIP4L="ZIP+4 code on Left"
			ZIP4R="ZIP+4 code on Right"
*/
       tgrf = open(fil, "rb");
       tgrfi = iter(tgrf);
 
       row=[];
       for lin in tgrfi:
         rrow=re.match("^(.)(....)(..........)(...)(....)(....)", lin)
	  row[len(row)]= {"RT": rrow[1], 
                  "VERSION": rrow[2],
                  "TLID": rrow[3],
                  "RTSEQ": rrow[4],
                  "ZIP4L": rrow[5],
                  "ZIP4R": rrow[6]};

	tgrf.close;
       return row;	


def getRTP(fil):
/*			RT="Record Type"
			VERSION="Version Number"
			FILECODE="File Code"
			CENID="Census File Identification Code"
			POLYID="Polygon Identification Code"
			POLYLONG="Polygon Internal Point Longitude"
			POLYLAT="Polygon Internal Point Latitude"
			WATER="Perennial/Intermittent Water Flag"
*/

         rrow=re.match("^(.)(....)(.....)(.....)(..........)(..........)(.........)(.)", lin)
	  row[len(row)]= {"RT": rrow[1], 
                  "VERSION": rrow[2],
                  "FILECODE": rrow[3],
                  "CENID": rrow[4],
                  "POLYID": rrow[5],
                  "POLYLONG": rrow[6]}
                  "POLYLAT": rrow[7]}
                  "WATER": rrow[8]};

	tgrf.close;
       return row;


def getF5I(fil):
/*
			RT="Record Type"
			VERSION="Version Number"
			FILE="File Code"
			TLID="TIGER Line ID, Permanent 1-Cell Number"
			RTLINK="Record Type of Link"
			CENIDL="Census File Identification Code, Left"
			POLYIDL="Polygon Identification Code, Left"
			CENIDR="Census File Identification Code, Right"
			POLYIDR="Polygon Identification Code, Right"
			FILLER="Reserved Space"
*/

         rrow=re.match("^(.)(....)(..........)(.....)(.)(.....)(..........)(.....)(..........)(.)", lin)
	  row[len(row)]= {"RT": rrow[1], 
                  "VERSION": rrow[2],
                  "TLID": rrow[3],
                  "FILE": rrow[4],
                  "RTLINK": rrow[5],
                  "CENIDL": rrow[6],
                  "POLYIDL": rrow[7],
                  "CENIDR": rrow[8],
                  "POLYIDR": rrow[9],
                  "FILLER": rrow[10]};

	tgrf.close;
       return row;


def getF5S(fil):
/*
			RT="Record Type"
			VERSION="Version Number"
			FILECODE="File Code"
			CENID="Census File Identification Code"
			POLYID="Polygon Identification Code"
		
			STATE="FIPS State Code, 1990"
			COUNTY="FIPS County Code, 1990"
			TRACT="Census Tract, 1990"
			BLOCK="Census Block Number, 1990"
			BLKGRP="Census Block Group, 1990"
			AIANHHFP="AIANHH FIPS 55 Code, 1990"
			AIANHH="AIANHH Census Code, 1990"
			AIHHTLI="AIHH Trust Land Indicator, 1990"
			ANRC="ANRC FIPS 55 Code, 1990"
			AITSCE="AITS Census Code, 1990"
			AITS="AITS FIPS 55 Code, 1990"
			CONCIT="Consolidated City FIPS 55 Code, 1990"
			COUSUB="County Subdivision FIPS 55 Code, 1990"
			SUBMCD="Subbarrio FIPS 55 Code, 1990"
			PLACE="Incorporated Place/CDP FIPS 55 Code, 1990"
			SDELM="Elementary School District Code, 1990"
			SDSEC="Secondary School District Code, 1990"
			SDUNI="Unified School District Code, 1990"
			MSACMSA="CMSA/MSA FIPS Code, 1990"
			PMSA="PMSA FIPS Code, 1990"
			NECMA="NECMA FIPS Code, 1990"
			CD101="101th Congressional District Code"
			CD103="103th Congressional District Code"
			BLOCKCOL="Census 1990 Collection Block Number"
			BLKCOLSUF="Census 1990 Collection Block Number Suffix"

			ZCTA5="5-Digit ZCTA, 1990"
			UR="Urban/Rural Indicator, 1990"
			UR90="Urban/Rural Indicator, 1990"
			VTD="Census Voting District Code, 1990"
			SLDU="State Legislative District Code (Upper Chamber), 1990"
			SLDL="State LEgislative District Code (Lower Chamber), 1990"
			UGA="Oregon Urban Growth Area, 1990"
*/

		input
			@1 RT $1.
			@2 VERSION $4.
			@6 FILECODE $5.
			@11 CENID $5.
			@16 POLYID $10.
		
			@26 WATER $1.
			@27 MSACMSA $4. 
			@31 PMSA $4.
			@35 AIANHH $5.
			@40 AIANHHCE $4.
			@44 AIHHTLI $1.
			@45 RS6 $2.
			@47 STATE $2.
			@49 COUNTY $3.
			@52 CONCIT $5.
			@57 COUSUB $5.
			@62 SUBMCD $5.
			@67 PLACE $5.
			@72 TRACT $6.
			@78 BLOCK $4.
			@82 CENSUS6 $1.
			@83 CDCU $2.
			@85 SLDU $3.
			@88 SLDL $3.
			@91 UGA $5.
			@96 BLKGRP $1.
			@97 VTD $6.
			@103 STATECOL $2.
			@105 COUNTYCOL $3.
			@108 BLOCKCOL $5.
			@113 BLKSUFCOL $1.
			@114 ZCTA5 $5.
			@119 UR $1.
			@120 UR90 $1.
			;
		tract = CASE WHEN tract > '' THEN substr(trimn(tract)||'00'),1,6) ELSE '' END;

def getF5E(fil):
		label
			RT="Record Type"
			VERSION="Version Number"
			FILECODE="File Code"
			CENID="Census File Identification Code"
			POLYID="Polygon Identification Code"
			STATEEC="FIPS State Code, 2002 Economic Census"
			COUNTYEC="FIPS County Code, 2002 Economic Census"
			RSE1="Reserved Space E1"
			RSE2="Reserved Space E2"
			PLACEEC="FIPS Economic Census Place Code, 2002 Economic Census"
			RSE3="Reserved Space E3"
			RSE4="Reserved Space E4"
			RSE5="Reserved Space E5"
			COMMREGEC="Commercial Region Code, 2002 Economic Census"
			RSE6="Reserved Space E6"
			;
		input
			@1 RT $1.
			@2 VERSION $4.
			@6 FILECODE $5. 
			@11 CENID $5.
			@16 POLYID $10.
			@26 STATEEC $2.
			@28 COUNTYEC $3.
			@31 RSE1 $5.
			@36 RSE2 $5.
			@41 PLACEEC $5.
			@46 RSE3 $5.
			@51 RSE4 $4.
			@55 RSE5 $1.
			@56 COMMREGEC $1.
			@57 RSE6 $17.
			;

def getF5C(fil):
		label
			RT="Record Type"
			VERSION="Version Number"
			STATE="FIPS State Code"
			COUNTY="FIPS County Code"
			DATAYR="FIPS Code, Name, and/or Attribute Data Applicable Year"
			FIPS="FIPS 55 Code"
			FIPSCC="FIPS 55 Class Code"
			PLACEDC="Place Description Code"
			LSADC="Legal/Statistical Area Description Code"
			ENTITY="Entity Type Code"
			MA="Metropolitan Area Code"
			SD="School District Code"
			AIANHHCE="Census AIANHH Code"
			VTDTRACT="Census Voting District Code/Census Tract Code"
			UAUGA="Urban Area Code/Urban Growth Area Code"
			AITSCE="Census AITS Code"
			NAME="Name of Geographical Area"
			;

		input
			@1 RT $1.
			@2 VERSION $4. 
			@6 STATE $2.  
			@8 COUNTY $3. 
			@11 DATAYR $4. 
			@15 FIPS $5. 
			@20 FIPSCC $2. 
			@22 PLACEDC $1. 
			@23 LSADC $2. 
			@25 ENTITY $1. 
			@26 MA $4. 
			@30 SD $5. 
			@35 AIANHHCE $4. 
			@39 VTDTRACT $6. 
			@45 UAUGA $5. 
			@50 AITSCE $3. 
			@53 NAME $60.;

def getF58(fil):
		label
			RT="Record Type"
			VERSION="Version Number"
			FILE="File Code"
			CENID="Census File ID"
			POLYID="Polygon ID"
			LAND="Landmark ID"
			;
		input
			@1 RT $1.
			@2 VERSION $4.
			@6 FILE $5.
			@11 CENID $5.
			@16 POLYID $10.
			@26 LAND $10.
			;

def getF5A(fil):
		infile "&filename." LRECL=211;
		label
			RT="Record Type"
			VERSION="Version Number"
			FILECODE="File Code"
			CENID="Census File Identification Code"
			POLYID="Polygon Identification Code"

			AIANHH90="AIANHH FIPS 55 Code, 1990"
			COUSUB90="County Subdivision FIPS 55 Code, Current"
			PLACE90="Incorporated Place FIPS 55 Code, Current"		

			TRACT90="Census Tract, 1990"
			BLOCK90="Census Block Number, 1990"
			CD101="Congressional District Code, Current (101th)"
			CD103="Congressional District Code, Current (103th)"

			SDELM="Elementary School District Code, Current"
			SDMID="Middle School District Code, Current"
			SDSEC="Secondary School District Code, Current"
			SDUNI="Unified School District Code, Current"

			TAZ="Traffic Analysis Zone Code, 1990"
			UA90="Urban Area, 1990"

			URBFLAG="Urban/Rural Flag"
			;
		input
			RT $ 1-1
			VERSION $ 2-5
			FILECODE $ 6-10
			CENID $ 11-15
			POLYID $ 16-25
			AIANHH90 $ 26-30
			COUSUB90 $31-35
			PLACE90 $ 36-40
			TRACT90 $ 41-46
			BLOCK90 $ 47-50
			CD101 $ 51-52
			CD103 $ 53-54
			SDELM $ 55-59
			SDMID $ 60-64
			SDSEC $ 65-69
			SDUNI $ 70-74
			TAZ $ 75-80
			UA $ 81-84
			URBFLAG $ 85-85
			;
			
		tract90 = CASE WHEN tract90 > '' THEN substr(trimn(tract90)||'00'),1,6) ELSE '' END;

def getF57(fil):
		label
			RT="Record Type"
			VERSION="Version Number"
			FILE="File Code"
			LAND="Land Identification Number"
			SOURCE="Source of Update"
			CFCC="Census Feature Class Code"
			LANAME="Landmark Name"
			LALONG="Longitude"
			LALAT="Latitude"
			;
		input
			@1 RT $1.
			@2 VERSION $4.
			@6 FILE $5.
			@11 LAND $10.
			@21 SOURCE $1.
			@22 CFCC $3.
			@25 LANAME $30.
			@55 LALONG $10.
			@65 LALAT $9.
			;

def getF55(fil):
		label
			RT="Record Type"
			VERSION="Version Number"
			FILECODE="File Code"
			FEAT="Line Name Identification Number"
			FEDIRP="Feature Direction, Prefix"
			FENAME="Feature Name"
			FETYPE="Feature Type"
			FEDIRS="Feature Direction, Suffix"
			;
		input
			@1 RT $1.
			@2 FILECODE $5.
			@7 FEAT $8.
			@15 FEDIRP $2.
			@17 FENAME $30.
			@47 FETYPE $4.
			@51 FEDIRS $2.
			;
	 version = '0005';   

def getF54(fil):
		label
			RT="Record Type"
			VERSION="Version Number"
			TLID="TIGER Line ID, Permanent 1-Cell Number"
			RTSQ="Record Sequence Number"
			FEAT1="Line Additional Name Identification Number, First"
			FEAT2="Line Additional Name Identification Number, Second"
			FEAT3="Line Additional Name Identification Number, Third"
			FEAT4="Line Additional Name Identification Number, Fourth"
			FEAT5="Line Additional Name Identification Number, Fifth"
			;
		input
			@1 RT $1.
			@2 VERSION $4.
			@6 TLID $10.
			@11 RTSQ $3.
			@19 FEAT1 $8.
			@27 FEAT2 $8.
			@35 FEAT3 $8.
			@43 FEAT4 $8.
			@51 FEAT5 $8.
			;
		
		  tlid = put(input(tlid, 10.), z10.);	

def getF53(fil):
		label
			RT="Record Type"
			VERSION="Version Number"
			TLID="TIGER/Line ID, Permanent 1-Cell Number"
			STATE80L="State FIPS Code, 1980 Left"
			STATE80R="State FIPS Code, 1980 Right"
			COUNTY80L="County FIPS Code, 1980 Left"
			COUNTY80R="County FIPS Code, 1980 Right"
			COUSUB80L="County Subdivision FIPS 55 Code, 1980 Left"
			COUSUB80R="County Subdivision FIPS 55 Code, 1980 Right"
			PLACE80L="Place/CDP FIPS 55 Code, 1980 Left"
			PLACE80R="Place/CDP FIPS 55 Code, 1980 Right"
			TRACT80L="Census Tract, 1980 Left"
			TRACT80R="Census Tract, 1980 Right"
			BLOCK80L="Census Block Number, 1980 Left"
			BLOCK80R="Census Block Number, 1980 Right"
			;

		input
			@1 RT $1. 
			@2 VERSION $4. 
			@6 TLID $10.
			@16 STATE80L $2. 
			@18 STATE80R $2. 
			@20 COUNTY80L $3. 
			@23 COUNTY80R $3. 
			@26 COUSUB80L $5. 
			@31 COUSUB80R $5. 
			@36 PLACE80L $5. 
			@41 PLACE80R $5. 
			@46 TRACT80L $6. 
			@52 TRACT80R $6. 
			@58 BLOCK80L $3. 
			@61 BLOCK80R $3. 
			;
		tlid = put(input(tlid, 10.), z10.);
		tract80l = CASE WHEN tract80l > '' THEN substr(trimn(tract80l)||'00'),1,6) ELSE '' END;
		tract80r = CASE WHEN tract80r > '' THEN substr(trimn(tract80r)||'00'),1,6) ELSE '' END;

def getF52(fil):
		label
			RT="Record Type"
			VERSION="Version Number"
			TLID="TIGER/LIne ID, Permanent 1-Cell Number"
			RTSQ="Record Sequence Number"
			LONG1="Point 1, Longitude"
			LAT1="Point 1, Latitude"
			LONG2="Point 2, Longitude"
			LAT2="Point 2, Latitude"
			LONG3="Point 3, Longitude"
			LAT3="Point 3, Latitude"
			LONG4="Point 4, Longitude"
			LAT4="Point 4, Latitude"
			LONG5="Point 5, Longitude"
			LAT5="Point 5, Latitude"
			LONG6="Point 6, Longitude"
			LAT6="Point 6, Latitude"
			LONG7="Point 7, Longitude"
			LAT7="Point 7, Latitude"
			LONG8="Point 8, Longitude"
			LAT8="Point 8, Latitude"
			LONG9="Point 9, Longitude"
			LAT9="Point 9, Latitude"
			LONG10="Point 10, Longitude"
			LAT10="Point 10, Latitude"
			;
		
		input
			@1 RT $1. 
			@2 VERSION $4. 
			@6 TLID $10.  
			@16 RTSQ $3. 
			@19 LONG1 $10. 
			@29 LAT1 $9. 
			@38 LONG2 $10. 
			@48 LAT2 $9. 
			@57 LONG3 $10. 
			@67 LAT3 $9. 
			@76 LONG4 $10. 
			@86 LAT4 $9. 
			@95 LONG5 $10. 
			@105 LAT5 $9. 
			@114 LONG6 $10. 
			@124 LAT6 $9. 
			@133 LONG7 $10. 
			@143 LAT7 $9. 
			@152 LONG8 $10. 
			@162 LAT8 $9. 
			@171 LONG9 $10. 
			@181 LAT9 $9. 
			@190 LONG10 $10. 
			@200 LAT10 $9.
			;
		  tlid = put(input(tlid, 10.), z10.);	

def getF51(fil):
		label
			RT="Record Type"
			VERSION="Version Number"
			TLID="TIGER/Line ID, Permanent 1-Cell Number"
			SIDE1="Single-Side Source Code"
			SOURCE="Linear Segment Source Code"
			FEDIRP="Feature Direction, Prefix"
			FENAME="Feature Name"
			FETYPE="Feature Type"
			FEDIRS="Feature Direction, Suffix"
			CFCC="Census Feature Class Code"
			FRADDL="Start Address, Left"
			TOADDL="End Address, Left"
			FRADDR="Start Address, Right"
			TOADDR="End Address, Right"
			FRIADDL="Start Imputed Address Flag, Left"
			TOIADDL="End Imputed Address Flag, Left"
			FRIADDR="Start Imputed Address Flag, Right"
			TOAIDDR="End Imputed Address Flag, Right"
			ZIPL="ZIP Code, Left"
			ZIPR="ZIP Code, Right"
			AIANHHFPL="AIANHH FIPS 55 Code, 1990 Left"
			AIANHHFPR="AIANHH FIPS 55 Code, 1990 Right"
			AIHHTLIL="AIHH Trust Land Indicator, 1990 Left"
			AIHHTLIR="AIHH Trust Land Indicator, 1990 Right"
			CENSUS1="Census Use 1"
			CENSUS2="Census Use 2"
			STATEL="State FIPS Code, 1990 Left"
			STATER="State FIPS Code, 1990 Right"
			COUNTYL="County FIPS Code, 1990 Left"
			COUNTYR="County FIPS Code, 1990 Right"
			COUSUBL="County Subdivision FIPS 55 Code, 1990 Left"
			COUSUBR="County Subdivision FIPS 55 Code, 1990 Right"
			SUBMCDL="Subbarrio FIPS 55 Code, 1990 Left"
			SUBMCDR="Subbarrio FIPS 55 Code, 1990 Right"
			PLACEL="Place/CDP FIPS 55 Code, 1990 Left"
			PLACER="Place/CDP FIPS 55 Code, 1990 Right"
			TRACTL="Census Tract, 1990 Left"
			TRACTR="Census Tract, 1990 Right"
			BLOCKL="Census Block Number, 1990 Left"
			BLOCKR="Census Block Number, 1990 Right"
			FRLONG="Start Longitude"
			FRLAT="Start Latitude"
			TOLONG="End Longitude"
			TOLAT="End Latitutde"
			;

		input
			@1 RT $1. 
			@2 VERSION $4. 
			@6 TLID $10.  
			@16 SIDE1 $1. 
			@17 SOURCE $1. 
			@18 FEDIRP $2. 
			@20 FENAME $30. 
			@50 FETYPE $4. 
			@54 FEDIRS $2. 
			@56 CFCC $3. 
			@59 FRADDL $11. 
			@70 TOADDL $11. 
			@81 FRADDR $11. 
			@92 TOADDR $11. 
			@103 FRIADDL $1. 
			@104 TOIADDL $1. 
			@105 FRIADDR $1. 
			@106 TOAIDDR $1. 
			@107 ZIPL $5. 
			@112 ZIPR $5. 
			@117 AIANHHFPL $5 
			@122 AIANHHFPR $5. 
			@127 AIHHTLIL $1. 
			@128 AIHHTLIR $1. 
			@129 CENSUS1 $1. 
			@130 CENSUS2 $1. 
			@131 STATEL $2. 
			@133 STATER $2. 
			@135 COUNTYL $3. 
			@138 COUNTYR $3. 
			@141 COUSUBL $5. 
			@146 COUSUBR $5. 
			@151 SUBMCDL $5. 
			@156 SUBMCDR $5. 
			@161 PLACEL $5. 
			@166 PLACER $5. 
			@171 TRACTL $6. 
			@177 TRACTR $6. 
			@183 BLOCKL $4. 
			@187 BLOCKR $4. 
			@191 FRLONG $10. 
			@201 FRLAT $9. 
			@210 TOLONG $10. 
			@220 TOLAT $9.
			;
		tlid = put(input(tlid, 10.), z10.);
		tractl = CASE WHEN tractl > '' THEN substr(trimn(tractl)||'00'),1,6) ELSE '' END;
		tractr = CASE WHEN tractr > '' THEN substr(trimn(tractr)||'00'),1,6) ELSE '' END;

