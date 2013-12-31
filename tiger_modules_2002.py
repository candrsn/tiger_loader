#tiger_modules_2002.py

class tiger:
   year = '';

   def _init_(self, yr):
      year = yr

   class RT1:
      
      def sqlddl():

      def get(filename):
         
	data thisRT1;
		infile "&filename." LRECL=229;
		label


      def longlabels:
         return {	RT: "Record Type",
        	VERSION: "Version Number",
	        TLID: "TIGER/Line ID, Permanent 1-Cell Number",
    	    SIDE1="Single-Side Source Code",
        	SOURCE="Linear Segment Source Code",
	        FEDIRP="Feature Direction, Prefix",
    	    FENAME="Feature Name",
        	FETYPE="Feature Type",
	        FEDIRS="Feature Direction, Suffix",
    	    CFCC="Census Feature Class Code",
        	FRADDL="Start Address, Left",
	        TOADDL="End Address, Left",
    	    FRADDR="Start Address, Right",
        	TOADDR="End Address, Right",
	        FRIADDL="Start Imputed Address Flag, Left",
    	    TOIADDL="End Imputed Address Flag, Left",
        	FRIADDR="Start Imputed Address Flag, Right",
	        TOAIDDR="End Imputed Address Flag, Right",
    	    ZIPL="ZIP Code, Left",
        	ZIPR="ZIP Code, Right",
	        AIANHHFPL="AIANHH FIPS 55 Code, 2000 Left",
    	    AIANHHFPR="AIANHH FIPS 55 Code, 2000 Right",
        	AIHHTLIL="AIHH Trust Land Indicator, 2000 Left",
	        AIHHTLIR="AIHH Trust Land Indicator, 2000 Right",
    	    CENSUS1="Census Use 1",
        	CENSUS2="Census Use 2",
	        STATEL="State FIPS Code, 2000 Left",
    	    STATER="State FIPS Code, 2000 Right",
        	COUNTYL="County FIPS Code, 2000 Left",
	        COUNTYR="County FIPS Code, 2000 Right",
    	    COUSUBL="County Subdivision FIPS 55 Code, 2000 Left",
        	COUSUBR="County Subdivision FIPS 55 Code, 2000 Right",
	        SUBMCDL="Subbarrio FIPS 55 Code, 2000 Left",
    	    SUBMCDR="Subbarrio FIPS 55 Code, 2000 Right",
        	PLACEL="Place/CDP FIPS 55 Code, 2000 Left",
	        PLACER="Place/CDP FIPS 55 Code, 2000 Right",
    	    TRACTL="Census Tract, 2000 Left",
        	TRACTR="Census Tract, 2000 Right",
	        BLOCKL="Census Block Number, 2000 Left",
    	    BLOCKR="Census Block Number, 2000 Right",
        	FRLONG="Start Longitude",
	        FRLAT="Start Latitude",
    	    TOLONG="End Longitude",
        	TOLAT="End Latitutde"};
			

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
	run;

%mend getRT1;


%macro getRT1(filename);
data thisRT1;
	infile "&filename." LRECL=229;
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
        AIANHHFPL="AIANHH FIPS 55 Code, 2000 Left"
        AIANHHFPR="AIANHH FIPS 55 Code, 2000 Right"
        AIHHTLIL="AIHH Trust Land Indicator, 2000 Left"
        AIHHTLIR="AIHH Trust Land Indicator, 2000 Right"
        CENSUS1="Census Use 1"
        CENSUS2="Census Use 2"
        STATEL="State FIPS Code, 2000 Left"
        STATER="State FIPS Code, 2000 Right"
        COUNTYL="County FIPS Code, 2000 Left"
        COUNTYR="County FIPS Code, 2000 Right"
        COUSUBL="County Subdivision FIPS 55 Code, 2000 Left"
        COUSUBR="County Subdivision FIPS 55 Code, 2000 Right"
        SUBMCDL="Subbarrio FIPS 55 Code, 2000 Left"
        SUBMCDR="Subbarrio FIPS 55 Code, 2000 Right"
        PLACEL="Place/CDP FIPS 55 Code, 2000 Left"
        PLACER="Place/CDP FIPS 55 Code, 2000 Right"
        TRACTL="Census Tract, 2000 Left"
        TRACTR="Census Tract, 2000 Right"
        BLOCKL="Census Block Number, 2000 Left"
        BLOCKR="Census Block Number, 2000 Right"
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
run;

%mend getRT1;


%macro getRT2(filename);
	data thisRT2;
		infile "&filename." LRECL=209;
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
	run;

%mend getRT2;


%macro getRT2(filename);
data thisRT2;
	infile "&filename." LRECL=209;
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
run;




%macro getRT4(filename);
    data thisRT4;
        infile "&filename." LRECL=59;
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
    run;
%mend getRT4;
%macro getRT4(filename);
    data thisRT4;
        infile "&filename." LRECL=59;
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
            RT $ 1-1
            VERSION $ 2-5
            TLID  6-15
            RTSQ $ 16-18
            FEAT1 $ 19-26
            FEAT2 $ 27-34
            FEAT3 $ 35-42
            FEAT4 $ 43-50
            FEAT5 $ 51-58
            ;
    run;
%mend getRT4;
%macro getRT5(filename);
    data thisRT5;
        infile "&filename." LRECL=57;
	LENGTH version $4.;
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
	 version = '0000';   
    run;
%mend getRT5;
%macro get_RT5(filename);
    data thisRT5;
        infile "&filename." LRECL=57;
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
            RT $ 1-1
            VERSION $ 2-5
            FILECODE $ 6-10
            FEAT $ 11-18
            FEDIRP $ 19-20
            FENAME $ 21-50
            FETYPE $ 51-54
            FEDIRS $ 55-56
            ;
    run;
%mend;
%macro getRT7(filename);
    data thisRT7;
        infile "&filename." LRECL=75;
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
    run;
%mend getRT7;
%macro getRT8(filename);
    data thisRT8;
        infile "&filename." LRECL=37;
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
    run;
%mend getRT8;

%macro getRTA(filename);
    data thisRTA;
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
            BLOCK90="Census Block Number, 2990"
            CD106="Congressional District Code, Current (106th)"
            CD108="Congressional District Code, Current (108th)"

            SDELM="Elementary School District Code, Current"
            PUMA5="Public Use Micrdata Area 5% File, 2000"
            SDSEC="Secondary School District Code, Current"
            SDUNI="Unified School District Code, Current"

            TAZ="Traffic Analysis Zone Code, 2000"
            UA="Urban Area, 2000"
            UA90="Urban Area, 1990"

            STATE90="FIPS State Code, 1990"
            COUNTY90="FIPS County Code, 1990"
            AIANHHCE90="AIANHH Census Code, 1990"	    
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
	    CD106 $ 51-52
	    CD108 $ 53-54
	    SDELM $ 55-59
	    PUMA5 $ 60-64
	    SDSEC $ 65-69
	    SDUNI $ 70-74
	    TAZ $ 75-80
	    UA $ 81-85
	    UA90 $ 86-89
	    STATE90 $ 90-91
	    COUNTY90 $92-94
	    AIANHHCE90 $ 95-98
            ;
    run;
%mend getRTA;
%macro getRTA(filename);
    data thisRTA;
        infile "&filename." LRECL=211;
        label
            RT="Record Type"
            VERSION="Version Number"
            FILECODE="File Code"
            CENID="Census File Identification Code"
            POLYID="Polygon Identification Code"
            STATECU="FIPS State Code, Current"
            COUNTYCU="FIPS County Code, Current"
            TRACT="Census Tract, 2000"
            BLOCK="Census Block Number, 2000"
            BLOCKSUFCU="Current Suffix for Census 2000 Block Number"
            RSA1="Reserved Space A1"
            AIANHHFPCU="AIANHH FIPS 55 Code, Current"
            AIANHHCU="AIANHH Census Code, Current"
            AIHHTLICU="AIHH Trust Land Indicator, Current"
            ANRCCU="ANRC FIPS 55 Code, Current"
            AITSCECU="AITS Census Code, Current"
            AITSCU="AITS FIPS 55 Code, Current"
            CONCITCU="Consolidated City FIPS 55 Code, Current"
            COUSUBCU="County Subdivision FIPS 55 Code, Current"
            SUBMCDCU="Subbarrio FIPS 55 Code, Current"
            PLACECU="Incorporated Place FIPS 55 Code, Current"
            SDELMCU="Elementary School District Code, Current"
            SDSECCU="Secondary School District Code, Current"
            SDUNICU="Unified School District Code, Current"
            RSA20="Reserved Space A20"
            RSA21="Reserved Space A21"
            RSA22="Reserved Space A22"
            CDCU="Congressional District Code, Current (109th)"
            ZCTA5CU="5-Digit ZCTA, Current"
            ZCTA3CU="3-Digit ZCTA, Current"
			RSA4="Reserved Space A4"
			RSA5="Reserved Space A5"
			RSA6="Reserved Space A6"
			RSA7="Reserved Space A7"
			RSA8="Reserved Space A8"
			RSA9="Reserved Space A9"
			CBSACU="Core Based Statistical Area Code, Current"
			CSACU="Combined Statistical Area Code, Current"
			NECTACU="New England City and Town Area Code, Current"
			CNECTACU="Combined New England City and Town Area Code, Current"
			METDIVCU="Metropolitan Division Code, Current"
			NECTADIVCU="New England City and Town Area Division Code, Current"
			RSA14="Reserved Space A14"
            UACU="Urban Area, Current"
            URCU="Urban/Rural Indicator, Current"
			RSA17="Reserved Space A17"
			RSA18="Reserved Space A18"
			RSA19="Reserved Space A19"
            ;
        input
            RT $ 1-1
            VERSION $ 2-5
            FILECODE $ 6-10
            CENID $ 11-15
            POLYID $ 16-25
            STATECU $ 26-27
            COUNTYCU $ 28-30
            TRACT $ 31-36
            BLOCK $ 37-40
            BLKSUFCU $ 41-41
			RSA1 $ 42-42
            AIANHHFPCU $ 43-47
            AIANHHCU $ 48-51
            AIHHTLICU $ 52-52
            ANRCCU $ 53-57
            AITSCECU $ 58-60
            AITSCU $ 61-65
            CONCITCU $ 66-70
            COUSUBCU $ 71-75
            SUBMCDCU $ 76-80
            PLACECU $ 81-85
            SDELMCU $ 86-90
            SDSECCU $ 91-95
            SDUNICU $ 96-100
			RSA20 $ 101-104
			RSA21 $ 105-108
			RSA22 $ 109-112
            CDCU $ 113-114
            ZCTA5CU $ 115-119
            ZCTA3CU $ 120-122
			RSA4 $ 123-128
			RSA5 $ 129-131
			RSA6 $ 132-134
			RSA7 $ 135-139
			RSA8 $ 140-145
			RSA9 $ 146-151
			CBSACU $ 152-156
			CSACU $ 157-159
			NECTACU $ 160-164
			CNECTACU $ 165-167
			METDIVCU $ 168-172
			NECTADIVCU $ 173-177
			RSA14 $ 178-181
            UACU $ 182-186
            URCU $ 187-187
			RSA17 $ 188-193
			RSA18 $ 194-199
			RSA19 $ 200-210
            ;
    run;
%mend getRTA;
%macro getRTC(filename);
    data thisRTC;
        infile "&filename." LRECL=123;
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
	run;
%mend getRTC;




%macro getRTC(filename);
    data thisRTC;
        infile "&filename." LRECL=123;
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
			AIANHH="Census AIANHH Code"
			VTDTRACT="Census Voting District Code/Census Tract Code"
			UAUGA="Urban Area Code/Urban Growht Area Code"
			AITSCE="Census AITS Code"
			CSACNECTA="Combined Statistical Area/Combined New England City and Town Area Code"
			CBSANECTA="CBSA Code, New England City and Town Area/Division Code, or Metropolitan Division"
			COMMREG="Commercial Region Code, Economic Census"
			RSC2="Reserved Space C2"
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
        	@35 AIANHH $4. 
	        @39 VTDTRACT $6. 
    	    @45 UAUGA $5. 
        	@50 AITSCE $3. 
	        @53 CSACNECTA $3. 
    	    @56 CBSANECTA $5. 
        	@61 COMMREG $1. 
	        @62 RSC2 $1. 
    	    @63 NAME $60.;
	run;
%mend getRTC;




%macro getRTE(filename);
    data thisRTE;
        infile "&filename." LRECL=74;
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
	run;
%mend getRTE;



%macro getRTH(filename);
    data thisRTH;
        infile "&filename." LRECL=63;
        label
            RT="Record Type"
            VERSION="Version Number"
            FILE="File Code"
	    TLID="TIGER Line ID, Permanent 1-Cell Number"
	    HIST="Last Source to Update"
	    SOURCE="First Source to Update"
	    TLIDFR1="TLID Created From 1"
	    TLIDFR2="TLID Created From 2"
	    TLIDTO1="TLID Became 1"
	    TLIDTO2="TLID Became 2"
            ;
	    
        input
        @1  RT      $ 1.
        @2  VERSION $ 4.
        @6  FILE    $ 5.
        @11 TLID    $10.
        @21 HIST    $ 1.
        @22 SOURCE  $ 1.
        @23 TLIDFR1 $10.
        @33 TLIDFR2 $10.
        @43 TLIDTO1 $10.
        @53 TLIDTO2 $10.;
	;
    run;
%mend getRTH;

%macro getRTI(filename);
    data thisRTI;
        infile "&filename." LRECL=128;
        label
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
            ;
	    
        input
        @1 RT $1.
        @2 VERSION $4.
	@6 TLID $10.
        @16 FILE $5.
        @21 RTLINK $1.
        @22 CENIDL $5.
        @27 POLYIDL $10.
        @37 CENIDR $5.
        @42 POLYIDR $10.
        @52 FILLER $1.
	;
    run;
%mend getRTI;
%macro getRTP(filename);
    data thisRTP;
        infile "&filename." LRECL=46;
		label
			RT="Record Type"
			VERSION="Version Number"
			FILECODE="File Code"
			CENID="Census File Identification Code"
			POLYID="Polygon Identification Code"
			POLYLONG="Polygon Internal Point Longitude"
			POLYLAT="Polygon Internal Point Latitude"
			WATER="Perennial/Intermittent Water Flag"
			;

		input
		@1 RT $1.
    	    	@2 VERSION $4.
        	@6 FILECODE $5. 
	        @11 CENID $5.
    	    	@16 POLYID $10.
        	@26 POLYLONG $10.
	        @36 POLYLAT $9.
    	    	@45 WATER $1.
			;
	run;
%mend getRTP;





libname INPUT "/data/master/tiger/2005/conversions/temp/testing/01_AL"; 

data INPUT.AL_rtP;
  infile "TGR01???.RTP";
  input @1 RT $1.
        @2 VERSION $4.
        @6 FILE $5. 
        @11 CENID $5.
        @16 POLYID $10.
        @26 POLYLONG $10.
        @36 POLYLAT $9.
        @45 WATER $1.;
run;




%macro getRTS(filename);
    data thisRTS;
        infile "&filename." LRECL=169;
        label
            RT="Record Type"
            VERSION="Version Number"
            FILECODE="File Code"
            CENID="Census File Identification Code"
            POLYID="Polygon Identification Code"
	    
            STATE="FIPS State Code, 2000"
            COUNTY="FIPS County Code, 2000"
            TRACT="Census Tract, 2000"
            BLOCK="Census Block Number, 2000"
            BLKGRP="Census Block Group, 2000"
            AIANHHFP="AIANHH FIPS 55 Code, 2000"
            AIANHH="AIANHH Census Code, 2000"
            AIHHTLI="AIHH Trust Land Indicator, 2000"
            ANRC="ANRC FIPS 55 Code, 2000"
            AITSCE="AITS Census Code, 2000"
            AITS="AITS FIPS 55 Code, 2000"
            CONCIT="Consolidated City FIPS 55 Code, 2000"
            COUSUB="County Subdivision FIPS 55 Code, 2000"
            SUBMCD="Subbarrio FIPS 55 Code, 2000"
            PLACE="Incorporated Place/CDP FIPS 55 Code, 2000"
            SDELM="Elementary School District Code, 2000"
            SDSEC="Secondary School District Code, 2000"
            SDUNI="Unified School District Code, 2000"
            MSACMSA="CMSA/MSA FIPS Code, 2000"
            PMSA="PMSA FIPS Code, 2000"
            NECMA="NECMA FIPS Code, 2000"
            CD106="106th Congressional District Code"
            CD108="108th Congressional District Code"
            PUMA5="PUMA - 5% File, 2000"
            PUMA1="PUMA - 1% File, 2000"
	    BLOCKCOL="Census 2000 Collection Block Number"
	    BLKCOLSUF="Census 2000 Collection Block Number Suffix"

            ZCTA5="5-Digit ZCTA, 2000"
            UR="Urban/Rural Indicator, 2000"
            UR90="Urban/Rural Indicator, 1990"
            VTD="Census Voting District Code, 2000"
            SLDU="State Legislative District Code (Upper Chamber), 2000"
            SLDL="State LEgislative District Code (Lower Chamber), 2000"
            UGA="Oregon Urban Growth Area, 2000"
            ;
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
    run;
%mend getRTS;
%macro get_RTS(filename);
    data thisRTS;
        infile "&filename." LRECL=169;
        label
            RT="Record Type"
            VERSION="Version Number"
            FILECODE="File Code"
            CENID="Census File Identification Code"
            POLYID="Polygon Identification Code"
            STATE="FIPS State Code, 2000"
            COUNTY="FIPS County Code, 2000"
            TRACT="Census Tract, 2000"
            BLOCK="Census Block Number, 2000"
            BLKGRP="Census Block Group, 2000"
            AIANHHFP="AIANHH FIPS 55 Code, 2000"
            AIANHH="AIANHH Census Code, 2000"
            AIHHTLI="AIHH Trust Land Indicator, 2000"
            ANRC="ANRC FIPS 55 Code, 2000"
            AITSCE="AITS Census Code, 2000"
            AITS="AITS FIPS 55 Code, 2000"
            CONCIT="Consolidated City FIPS 55 Code, 2000"
            COUSUB="County Subdivision FIPS 55 Code, 2000"
            SUBMCD="Subbarrio FIPS 55 Code, 2000"
            PLACE="Incorporated Place/CDP FIPS 55 Code, 2000"
            SDELM="Elementary School District Code, 2000"
            SDSEC="Secondary School District Code, 2000"
            SDUNI="Unified School District Code, 2000"
            MSACMSA="CMSA/MSA FIPS Code, 2000"
            PMSA="PMSA FIPS Code, 2000"
            NECMA="NECMA FIPS Code, 2000"
            CD106="106th Congressional District Code"
            CD108="108th Congressional District Code"
            PUMA5="PUMA - 5% File, 2000"
            PUMA1="PUMA - 1% File, 2000"
            ZCTA5="5-Digit ZCTA, 2000"
            ZCTA3="3-Digit ZCTA, 2000"
            TAZ="Traffic Analysis Zone Code, 2000"
            TAZCOMB="TAZ-State Combined (Not Filled), 2000"
            UA="Urban Area, 2000"
            UR="Urban/Rural Indicator, 2000"
            VTD="Census Voting District Code, 2000"
            SLDU="State Legislative District Code (Upper Chamber), 2000"
            SLDL="State LEgislative District Code (Lower Chamber), 2000"
            UGA="Oregon Urban Growth Area, 2000"
            ;
        input
            RT $ 1-1
            VERSION $ 2-5
            FILECODE $ 6-10
            CENID $ 11-15
            POLYID $ 16-25
            STATE $ 26-27
            COUNTY $ 28-30
            TRACT $ 31-36
            BLOCK $ 37-40
            BLKGRP $ 41-41
            AIANHHFP $ 42-46
            AIANHH $ 47-50
            AIHHTLI $ 51-51
            ANRC $ 52-56
            AITSCE $ 57-59
            AITS $ 60-64
            CONCIT $ 65-69
            COUSUB $ 70-74
            SUBMCD $ 75-79
            PLACE $ 80-84
            SDELM $ 85-89
            SDSEC $ 90-94
            SDUNI $ 95-99
            MSACMSA $ 100-103
            PMSA $ 104-107
            NECMA $ 108-111
            CD106 $ 112-113
            CD108 $ 114-115
            PUMA5 $ 116-120
            PUMA1 $ 121-125
            ZCTA5 $ 126-130
            ZCTA3 $ 131-133
            TAZ $ 134-139
            TAZCOMB $ 140-145
            UA $ 146-150
            UR $ 151-151
            VTD $ 152-157
            SLDU $ 158-160
            SLDL $ 161-163
            UGA $ 164-168
            ;
    run;
%mend;
%macro getRTZ(filename);
    data thisRTZ;
        infile "&filename." LRECL=30;
		label
			RT="Record Type"
			VERSION="Version Number"
			TLID="TIGER Line ID
			RTSQ="Record Sequence Number"
			ZIP4L="ZIP+4 code on Left"
			ZIP4R="ZIP+4 code on Right"
			;

		input
		@1 RT $1.
	        @2 VERSION $4. 
    	 	@6 TLID $10.  
        	@16 RTSQ $3. 
	        @19 ZIP4L $4. 
		@23 ZIP4R $4.
		;
	run;
%mend getRTZ;


