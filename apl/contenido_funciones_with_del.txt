==================================================
FUNCTION: ALLFNS
==================================================
∇ ALLFNS PN;NL;I;AA;⎕IO;ML;PAGE;M;J;X;Y;P                       
⍝ PRINTS A LISTING OF THE PROCEDURES IN THE ACTIVE WORKSPACE, 
⍝ EXCEPT FOR ITSELF AND  LISTFN.  THE FIRST PAGE IS A LIST    
⍝ OF THE NAMES OF THE PROCEDURES.  IT IS ASSUMED THAT THE     
⍝ THE TERMINAL PRINTS 66 LINES PER PAGE.  THE ARGUMENT  PN  IS
⍝ THE FIRST PAGE NUMBER OF THE LISTING TO BE PRINTED.         
⍝ NORMALLY  PN IS 1.                                          
 P←1                                                          
 NL←⎕NL 3                                                     
 ⎕IO←1                                                        
 M←(⍴NL)[2]                                                   
 I←M+1                                                        
LOOP1:→(0≥I←I-1)/LIST                                         
 NL←NL[⍋⎕AV⍳NL[;I];]                                          
 →LOOP1                                                       
LIST:ML←((1↑⍴NL),15)↑NL                                       
 ML←(ML∨.≠'ALLFNS         ')⌿ML                               
 ML←(ML∨.≠'LISTFN         ')⌿ML                               
 PAGE←52 0⍴''                                                 
LOOP2:→(0≥1↑⍴ML)/OK                                           
 PAGE←PAGE,52 15↑ML                                           
 ML←52 0↓ML                                                   
 →LOOP2                                                       
OK:→(P<PN)/SKIP0                                              
 (25⍴' '),'THE PROCEDURES'                                    
 ' '                                                          
 PAGE                                                         
 12 1⍴' '                                                     
SKIP0:I←0                                                     
 PAGE←0 65⍴' '                                                
LOOP:→((1↑⍴NL)<I←I+1)/END                                     
 →(∧/'ALLFNS'=6↑NL[I;])/LOOP                                  
 →(∧/'LISTFN'=6↑NL[I;])/LOOP                                  
 →(0=1↑⍴AA←LISTFN NL[I;])/LOOP                                
 X←65↓AA[1;]                                                  
 →(∧/X=' ')/ADD                                               
 J←65-+/∧\∼⌽';'=Y←65↑AA[1;]                                   
 AA[1;J+⍳65-J]←' '                                            
 AA←(2≠⍳1+1↑⍴AA)⍀AA                                           
 AA[2;]←(1↓⍴AA)↑(10⍴' '),(J↓Y),X                              
ADD:PAGE←PAGE,[1]((2+1↑⍴AA),65)↑AA                            
PRINT:→(46≥1↑⍴PAGE)/LOOP                                      
 P←P+1                                                        
 →(57≤1↑⍴PAGE)/PARTIAL                                        
 →(P<PN)/SKIP1                                                
 66 65↑PAGE                                                   
SKIP1:PAGE←0 65⍴' '                                           
 →LOOP                                                        
PARTIAL:→(P<PN)/SKIP2                                         
 52 65↑PAGE                                                   
 14 1⍴' '                                                     
SKIP2:PAGE←52 0↓PAGE                                          
 →PRINT                                                       
 →LOOP                                                        
END:PAGE
∇
==================================================
FUNCTION: CCONJ
==================================================
∇ B←CCONJ A                                   
⍝ COMPUTES THE CONJUGATE OF A COMPLEX ARRAY.
 →NOTEST/BEGIN                              
 A←CNRMLZ A                                 
BEGIN:B←A×(⍴A)⍴1 ¯1
∇
==================================================
FUNCTION: CDIFF
==================================================
∇ C←A CDIFF B                                     
⍝ COMPUTES THE DIFFERENCE OF TWO COMPLEX ARRAYS.
 C←A CSUM-B
∇
==================================================
FUNCTION: CINV
==================================================
∇ B←CINV A                                     
⍝ COMPUTES THE RECIPROCAL OF A COMPLEX ARRAY.
 B←1 0 CQUOT A
∇
==================================================
FUNCTION: CMAG
==================================================
∇ B←CMAG A                                    
⍝ COMPUTES THE MAGNITUDE OF A COMPLEX ARRAY.
 B←(CNORM A)⋆0.5
∇
==================================================
FUNCTION: CMATPROD
==================================================
∇ C←A CMATPROD B;⎕IO;X;AX;BX;RR;NOTEST;RA;RB           
⍝ COMPUTES THE MATRIX PRODUCT OF TWO NONSCALAR ARRAYS
⍝ OF COMPLEX NUMBERS.                                
 NOTEST←0                                            
 ⎕IO←1                                               
 A←CNRMLZ A                                          
 B←CNRMLZ B                                          
 DERR(∧/1<(⍴⍴A),⍴⍴B)∧(⍴A)[¯1+⍴⍴A]=1↑⍴B               
 C←((RA←¯2↓⍴A),(RB←¯1↓1↓⍴B),2)⍴0                     
 NOTEST←1                                            
 X←1=⍳1↑⍴B                                           
 RR←((⍴RA)+⍳⍴RB),(⍳⍴RA),⍴⍴C                          
LOOP:AX←RR⍉(RB,RA,2)⍴X/[¯1+⍴⍴A]A                     
 C←C CSUM AX CPROD(⍴C)⍴X⌿B                           
 →(∼1↑X←¯1⌽X)/LOOP
∇
==================================================
FUNCTION: CNORM
==================================================
∇ B←CNORM A                         
⍝ COMPUTES THE COMPLEX NORM OF  A.
 →NOTEST/BEGIN                    
 A←CNRMLZ A                       
BEGIN:B←+/A×A
∇
==================================================
FUNCTION: CNRMLZ
==================================================
∇ B←CNRMLZ A                                  
⍝ COMPUTES THE STANDARD FORM FOR AN ARRAY OF
⍝ COMPLEX NUMBERS.                          
 →NOTEST/BEGIN                              
 DERR(0=⍴⍴A)∨(¯1↑⍴A)ϵ1 2                    
BEGIN:B←((¯1↓⍴A),2)↑A
∇
==================================================
FUNCTION: CPOWER
==================================================
∇ C←A CPOWER B;RHO;RC;I;J;NOTEST               
⍝ COMPUTES THE B-TH POWER OF THE COMPLEX     
⍝ ARRAY  A  USING THE BINARY POWER ALGORITHM.
 NOTEST←0                                    
 A←CNRMLZ A                                  
 DERR∧/(,B=⌊B),,B≥0                          
 B←((⍴B),1)⍴B                                
 EXPANDV                                     
 NOTEST←1                                    
 RC←(×/¯1↓RHO←⍴A),2                          
 A←RC⍴A                                      
 C←RC⍴1 0                                    
 I←(B>0)/⍳⍴B←,B                              
LOOP:C[J;]←C[J;]CPROD A[J←(2|B[I])/I;]       
 →(0=⍴I←(B[I]≥2)/I)/END                      
 A[I;]←A[I;]CPROD A[I;]                      
 B[I]←⌊B[I]÷2                                
 →LOOP                                       
END:C←RHO⍴C
∇
==================================================
FUNCTION: CPROD
==================================================
∇ C←A CPROD B;R                                
⍝ COMPUTES THE PRODUCT OF TWO COMPLEX ARRAYS.
 →NOTEST/BEGIN                               
 A←CNRMLZ A                                  
 B←CNRMLZ B                                  
 EXPANDV                                     
BEGIN:C←(R⍴-/A×B),(R←(¯1↓⍴A),1)⍴+/A×⌽B       
 C←C×(|C)≥EPSILON×⌈/,|C
∇
==================================================
FUNCTION: CPRODRED
==================================================
∇ C←CPRODRED A;⎕IO;RHO;D;E;CC;L;NOTEST           
⍝ COMPUTES THE PRODUCT REDUCTION ALONG THE LAST
⍝ AXIS OF AN ARRAY OF COMPLEX NUMBERS.         
 NOTEST←0                                      
 A←CNRMLZ A                                    
 →(1=⍴⍴C←A)/0                                  
 ⎕IO←1                                         
 L←×/RHO←¯2↓⍴C                                 
 C←(L,¯2↑⍴C)⍴C                                 
 →(0=(⍴C)[2])/ZERO                             
 NOTEST←1                                      
LOOP:→(1=D←(⍴C)[2])/ONE                        
 CC←((L,E,2)↑C)CPROD(L,(-E←⌊D÷2),2)↑C          
 C←CC,[2]C[;(E+1)×⍳D≠2×E;]                     
 →LOOP                                         
ZERO:C←(RHO,2)⍴1 0                             
 →0                                            
ONE:C←(RHO,2)⍴C
∇
==================================================
FUNCTION: CQUOT
==================================================
∇ C←A CQUOT B;N;R                               
⍝ COMPUTES THE QUOTIENT OF TWO COMPLEX ARRAYS.
 →NOTEST/BEGIN                                
 A←CNRMLZ A                                   
 B←CNRMLZ B                                   
 EXPANDV                                      
BEGIN:DERR∧/,0≠N←(R←(¯1↓⍴B),1)⍴+/B×B          
 C←((R⍴+/A×B)÷N),(R⍴-/B×⌽A)÷N                 
 C←C×(|C)≥EPSILON×⌈/,|C
∇
==================================================
FUNCTION: CSUM
==================================================
∇ C←A CSUM B                               
⍝ COMPUTES THE SUM OF TWO COMPLEX ARRAYS.
 →NOTEST/BEGIN                           
 A←CNRMLZ A                              
 B←CNRMLZ B                              
 EXPANDV                                 
BEGIN:C←C×(|C)≥EPSILON×⌈/,|C←A+B
∇
==================================================
FUNCTION: DAQ
==================================================
∇ X←DAQ A;NA;RA;M;K;R                             
⍝ PRODUCES THE CHARACTER ARRAY FOR DISPLAYING AN
⍝ ARRAY OF RATIONAL NUMBERS.                    
 X←''                                           
 →(0=NA←×/⍴A)/0                                 
 RA←⍴A←QNRMLZ A                                 
 M←1⌈¯1↓¯2↑RA                                   
 K←¯1↑⍴X←⍕(NA,1)⍴A                              
 R←(¯1++/X=' ')×NA⍴0 1                          
 X←R⌽X                                          
 X←((×/¯1↓RA),2×K)⍴X                            
 X[;K+⎕IO]←'/'                                  
 X←X,' '                                        
 X←((¯2↓RA),M×¯1↑⍴X)⍴X
∇
==================================================
FUNCTION: DARV
==================================================
∇ X←P DARV A;NA;RA;M;K                              
⍝ PRODUCES THE CHARACTER ARRAY DISPLAYING AN ARRAY
⍝ OF REAL VECTORS WITH P DECIMAL PLACES.          
 X←''                                             
 →(0=NA←×/RA←⍴A)/0                                
 M←1⌈¯1↓¯2↑RA                                     
 K←¯1↑⍴X←P⍕(NA,1)⍴A                               
 X←((×/¯1↓RA),K×¯1↑RA)⍴X                          
 X←(0 2+⍴X)↑X                                     
 X←((¯2↓RA),M×¯1↑⍴X)⍴X
∇
==================================================
FUNCTION: DAZV
==================================================
∇ X←DAZV A                                           
⍝ PRODUCES THE CHARACTER ARRAY DISPLAYING AN ARRAY 
⍝ OF INTEGER VECTORS OR REAL VECTORS ROUNDED TO THE
⍝ NEAREST INTEGER.                                 
 X←''                                              
 →(0=×/⍴A)/0                                       
 X←0 DARV A
∇
==================================================
FUNCTION: DECCARRY
==================================================
∇ Z←DECCARRY X;SGN          
⍝ EXERCISE 2.5.2          
 Z←,X                     
 SGN←1                    
LOOP:Z←(+/∧\Z=0)↓Z        
 →(0≠⍴Z)/NONEMPTY         
 →Z←,0                    
NONEMPTY:→(0<1↑Z)/POS     
 SGN←-SGN                 
 Z←-Z                     
POS:→(∧/(0≤Z),Z<10)/DONE  
 Z←(0,10|Z)+(Z ZQUOT 10),0
 →LOOP                    
DONE:Z←SGN×Z
∇
==================================================
FUNCTION: DECDIFF
==================================================
∇ Z←X DECDIFF Y   
⍝ EXERCISE 2.5.3
 Z←X DECSUM-Y
∇
==================================================
FUNCTION: DECPROD
==================================================
∇ Z←X DECPROD Y;⎕IO;U;V     
⍝ EXERCISE 2.5.2          
 ⎕IO←0                    
 U←(Y←,Y)∘.×X←,X          
 V←(-⍳⍴Y)⌽((⍴U)+0,¯1+⍴Y)↑U
 Z←DECCARRY+⌿V
∇
==================================================
FUNCTION: DECQUOT
==================================================
∇ Z←X DECQUOT Y;SGNX;SGNY;L;U  
⍝ EXERCISE 2.5.3             
 SGNX←×1↑X←DECCARRY X        
 SGNY←×1↑Y←DECCARRY Y        
 →(SGNY≠0)/NONZERO           
 →(SGNX≠0)/DE                
 Z←,1                        
 →0                          
DE:'DOMAIN ERROR'            
 →0                          
NONZERO:X←|X                 
 Y←|Y                        
 Z←,0                        
LOOP:→(0>L←(⍴X)-⍴Y)/DONE     
 →(∧/0=U←((-L)↓X)-Y)/SUBTRACT
 →(0<U[(U≠0)⍳1])/SUBTRACT    
 →(0=L)/DONE                 
 L←L-1                       
SUBTRACT:X←X DECDIFF Y,L⍴0   
 Z←Z DECSUM 1,L⍴0            
 →LOOP                       
DONE:Z←Z×SGNX×SGNY           
 →((SGNX=1)∨∧/X=0)/0         
 Z←Z DECDIFF SGNY
∇
==================================================
FUNCTION: DECSUM
==================================================
∇ Z←X DECSUM Y;M            
⍝ EXERCISE 2.5.2          
 M←(⍴X←,X)⌈⍴Y←,Y          
 Z←DECCARRY((-M)↑X)+(-M)↑Y
∇
==================================================
FUNCTION: DERR
==================================================
∇ DERR T                                                
⍝ IF  T  IS FALSE, A MESSAGE IS PRINTED AND ALL ACTIVE
⍝ PROCEDURES ARE TERMINATED.                          
 →T/0                                                 
 'PROCEDURE DOMAIN ERROR'                             
 →
∇
==================================================
FUNCTION: DESCRIBE
==================================================
∇ DESCRIBE                                             
 'THE PROCEDURES IN THIS LIBRARY MAY BE USED TO'     
 'MAINTAIN THE LIBRARY CLASSLIB.  THE PROCEDURE'     
 'ALLFNS LISTS ALL FUNCTIONS IN THE ACTIVE WORKSPACE'
 'ON A HARCOPY TERMINAL WHICH PRINTS 66 LINES PER'   
 'PAGE.  THE PROCEDURE NOCOMS REMOVES ALL COMMENTS'  
 'FROM ALL PROCEDURES IN THE ACTIVE WORKSPACE.  THE' 
 'PROCEDURE MAKEBIG CONSTRUCTS THE ARRAYS BIGPRIMES' 
 'AND BIGINV USED BY MPZDET.'
∇
==================================================
FUNCTION: EXPAND
==================================================
∇ EXPAND;RA;NA;RB;NB                                         
⍝ PROCEDURE TO TEST IF THE GLOBAL VARIABLES  A  AND  B  ARE
⍝ CONFORMABLE FOR SCALAR OPERATIONS AND IF SO, TO EXPAND   
⍝ ONE OF THEM, IF NECESSARY, SO THAT THEY HAVE THE SAME    
⍝ SHAPE.  IF THEY ARE NOT CONFORMABLE, ALL PROCESSING IS   
⍝ STOPPED.  IF EITHER  A  OR  B  HAS ONE ENTRY, THEY ARE   
⍝ CONFOMRABLE.                                             
 →(∨/1=(NA←×/RA←⍴A),NB←×/RB←⍴B)/EXP                        
⍝ OTHERWISE, THEY MUST HAVE THE SAME RANK.                 
 →((⍴RA)≠⍴RB)/RNKERR                                       
⍝ AND THE SAME SHAPE.                                      
 →(∨/RA≠RB)/LENERR                                         
 →0                                                        
RNKERR:'PROCEDURE RANK ERROR'                              
 →                                                         
LENERR:'PROCEDURE LENGTH ERROR'                            
 →                                                         
⍝ SEE WHICH ARRAY MUST BE EXPANDED.                        
EXP:→((NA≠1)∨(NA=1)∧(NB=1)∧(⍴RA)>⍴RB)/EXB                  
⍝ EXPAND A                                                 
 →0,⍴A←RB⍴A                                                
⍝ EXPAND B                                                 
EXB:B←RA⍴B
∇
==================================================
FUNCTION: EXPANDV
==================================================
∇ EXPANDV;RA;NA;RB;NB                                    
⍝ TESTS IF TWO ARRAYS OF VECTORS ARE CONFORMABLE FOR   
⍝ SCALAR OPERATIONS AND IF SO, EXPANDS ONE, IF         
⍝ NECESSARY, SO THAT THEY HAVE THE SAME SHAPE ALONG ALL
⍝ BUT THE LAST AXIS.  IF THEY ARE NOT CONFORMABLE, ALL 
⍝ PROCESSING IS STOPPED.                               
⍝ SCALARS ARE REPLACED BY VECTORS OF LENGTH 1.         
 →(1≤⍴⍴A)/CHECKB                                       
 A←,A                                                  
CHECKB:→(1≤⍴⍴B)/NEXT                                   
 B←,B                                                  
⍝ IF  A  OR  B  HAS ONE ENTRY, THE ARE CONFORMABLE.    
NEXT:→(∨/1=(NA←×/RA←¯1↓⍴A),NB←×/RB←¯1↓⍴B)/EXP          
 →((⍴RA)≠⍴RB)/RNKERR                                   
 →(∨/RA≠RB)/LENERR                                     
 →0                                                    
RNKERR:'VECTOR RANK ERROR'                             
 →                                                     
LENERR:'VECTOR LENGTH ERROR'                           
 →                                                     
EXP:→((NA≠1)∨(NA=1)∧(NB=1)∧(⍴RA)>⍴RB)/EXPB             
 A←(RB,¯1↑⍴A)⍴A                                        
 →0                                                    
EXPB:B←(RA,¯1↑⍴B)⍴B
∇
==================================================
FUNCTION: FIRSTPRIME
==================================================
∇ P←FIRSTPRIME N        
⍝ EXERCISE 2.4.5      
 →(N>2)/ODD           
 P←2                  
 →0                   
ODD:P←1+2×⌊N÷2        
LOOP:→(1=⍴ZFACTOR P)/0
 P←P+2                
 →LOOP
∇
==================================================
FUNCTION: FRCLEAR
==================================================
∇ FRCLEAR;I                                              
⍝ EXPUNGES THE VARIABLES DESCRIBING THE CURRENT        
⍝ FINITE RING.                                         
 I←(⎕EX'FRPLUS'),(⎕EX'FRTIMES'),(⎕EX'FRNEG'),⎕EX'FRINV'
∇
==================================================
FUNCTION: FRDET
==================================================
∇ D←FRDET A;⎕IO;M;N;K;SIGN;X;NX;S;T;SGN;CFR;U                 
⍝ COMPUTES THE DETERMINANT OF A MATRIX OVER THE FINITE RING,
⍝ WHICH MUST BE COMMUTATIVE.                                
 ⎕IO←0                                                      
 DERR∧/(FRTEST A),(2=⍴⍴A),=/⍴A                              
 DERR∧/,FRTIMES=⍉FRTIMES                                    
 T←(2⋆N←1↑⍴A)⍴3-3                                           
 CFR←⍴FRNEG                                                 
 M←A[K←0;]                                                  
 SIGN←1                                                     
 NX←+/2⋆X←(N,1)⍴⍳N                                          
LOOP:→(N≤K←K+1)/END                                         
 T[NX]←⍳⍴NX                                                 
 NX←+/2⋆X←(K+1)SSUB N                                       
 S←T[(⍉((K+1),⍴NX)⍴NX)-2⋆X]                                 
 SIGN←-SIGN                                                 
 U←(,FRTIMES)[A[K;X]+M[S]×CFR]                              
 M←(¯1↓⍴U)⍴0                                                
 X←0=⍳¯1↑⍴U                                                 
 SGN←SIGN                                                   
LOOP2:→(SGN=¯1)/NEG                                         
 M←(,FRPLUS)[((⍴M)⍴X/U)+M×CFR]                              
 →INCR                                                      
NEG:M←(,FRPLUS)[FRNEG[(⍴M)⍴X/U]+M×CFR]                      
INCR:SGN←-SGN                                               
 →(∼1↑X←¯1⌽X)/LOOP2                                         
 →LOOP                                                      
END:D←+/M
∇
==================================================
FUNCTION: FRDIFF
==================================================
∇ C←A FRDIFF B;⎕IO                                       
⍝ COMPUTES THE DIFFERENCE OF TWO ARRAYS OVER THE FINITE
⍝ RING.                                                
 ⎕IO←0                                                 
 →NOTEST/BEGIN                                         
 DERR(FRTEST A)∧FRTEST B                               
 EXPAND                                                
BEGIN:C←(,FRPLUS)[FRNEG[B]+A×1↑⍴FRPLUS]
∇
==================================================
FUNCTION: FRINIT
==================================================
∇ A FRINIT B;⎕IO;C;U                                       
⍝ INITIALIZES THE GLOBAL VARIABLES FOR THE CURRENT FINITE
⍝ RING.  A  IS THE ADDITION TABLE AND  B  IS THE         
⍝ MULTIPLICATION TABLE.                                  
 FRPLUS←A                                                
 FRTIMES←B                                               
 FRNEG←SFEL A=⎕IO←0                                      
 U←FRINV/⍳⍴FRINV←(∨/⍉C)∧∨/C←B=1                          
 FRINV[U]←SFEL C[U;]
∇
==================================================
FUNCTION: FRMATPROD
==================================================
∇ C←A FRMATPROD B;M;RHO;RR;X;AX;BX;⎕IO;RA;RB             
⍝ COMPUTES THE MATRIX PRODUCT OF TWO NONSCALAR ARRAYS  
⍝ OVER THE FINITE RING.                                
 ⎕IO←0                                                 
 DERR(FRTEST A)∧(FRTEST B)∧(∧/0<(⍴⍴A),⍴⍴B)∧(¯1↑⍴A)=1↑⍴B
 RHO←(RA←¯1↓⍴A),RB←1↓⍴B                                
 RR←((⍴RA)+⍳⍴RB),⍳⍴RA                                  
 C←RHO⍴0                                               
 M←1↑⍴FRTIMES                                          
 X←(1↑⍴B)↑1                                            
LOOP:AX←RR⍉(RB,RA)⍴X/A                                 
 BX←RHO⍴X⌿B                                            
 C←(,FRPLUS)[(,FRTIMES)[BX+AX×M]+C×M]                  
 →(∼1↑X←¯1⌽X)/LOOP
∇
==================================================
FUNCTION: FRPOWER
==================================================
∇ C←A FRPOWER B;RHO;I;J;⎕IO;M                        
⍝ COMPUTES THE B-TH POWER OF  A  IN THE FINITE RING
⍝ USING THE BINARY POWER ALGORITHM.                
 ⎕IO←0                                             
 DERR(FRTEST A)∧∧/,(B=⌊B),B≥0                      
 EXPAND                                            
 RHO←⍴A                                            
 C←(⍴A←,A)⍴1                                       
 I←(B>0)/⍳⍴B←,B                                    
 M←1↑⍴FRTIMES                                      
LOOP:C[J]←(,FRTIMES)[A[J]+M×C[J←(2|B[I])/I]]       
 →(0=⍴I←(B[I]≥2)/I)/END                            
 A[I]←(,FRTIMES)[A[I]×M+1]                         
 B[I]←⌊B[I]÷2                                      
 →LOOP                                             
END:C←RHO⍴C
∇
==================================================
FUNCTION: FRPROD
==================================================
∇ C←A FRPROD B;⎕IO                                          
⍝ COMPUTES THE PRODUCT OF TWO ARRAYS OVER THE FINITE RING.
 ⎕IO←0                                                    
 →NOTEST/BEGIN                                            
 DERR(FRTEST A)∧FRTEST B                                  
 EXPAND                                                   
BEGIN:C←(,FRTIMES)[B+A×1↑⍴FRTIMES]
∇
==================================================
FUNCTION: FRSUM
==================================================
∇ C←A FRSUM B;⎕IO                                       
⍝ COMPUTES THE SUM OF TWO ARRAYS OVER THE FINITE RING.
 ⎕IO←0                                                
 →NOTEST/BEGIN                                        
 DERR(FRTEST A)∧FRTEST B                              
 EXPAND                                               
BEGIN:C←(,FRPLUS)[B+A×1↑⍴FRPLUS]
∇
==================================================
FUNCTION: FRTEST
==================================================
∇ T←FRTEST A                                               
⍝ CHECKS WHETHER  A  REPRESENTS AN ARRAY OVER THE CURRENT
⍝ FINITE RING.                                           
 T←∧/(,A=⌊A),(,A<⍴FRNEG),,0≤A
∇
==================================================
FUNCTION: FRXDEGREE
==================================================
∇ B←FRXDEGREE A                                             
⍝ COMPUTES THE ARRAY OF DEGREES OF AN ARRAY OF POLYNOMIALS
⍝ OVER THE FINITE RING.                                   
 DERR FRTEST A                                            
 B←ZXDEGREE A
∇
==================================================
FUNCTION: FRXDIFF
==================================================
∇ C←A FRXDIFF B                                         
⍝ COMPUTES THE DIFFERENCE OF TWO ARRAYS OF POLYNOMIALS
⍝ OVER THE FINITE RING.                               
 C←A FRXSUM FRNEG[B]
∇
==================================================
FUNCTION: FRXEVAL
==================================================
∇ Y←A FRXEVAL B;I;⎕IO;RHO;M                                
⍝ EVALUTES THE POLYNOMIALS IN  A  AT  B  IN THE          
⍝ FINITE RING.  COMMUTATIVITY OF THE RING IS NOT CHECKED.
 DERR(FRTEST A)∧FRTEST B←((⍴B),1)⍴B                      
 EXPANDV                                                 
 A←((×/RHO←¯1↓⍴A),¯1↑⍴A)⍴A                               
 Y←(⍴B←,B)⍴⎕IO←0                                         
 M←1↑⍴FRPLUS                                             
 I←(⍴A)[1]                                               
LOOP:→(0>I←I-1)/END                                      
 Y←(,FRPLUS)[(,FRTIMES)[B+M×Y]+M×A[;I]]                  
 →LOOP                                                   
END:Y←RHO⍴Y
∇
==================================================
FUNCTION: FRXLEAD
==================================================
∇ C←FRXLEAD A;EPSILON                               
⍝ COMPUTES THE LEADING COEFFICIENTS OF AN ARRAY OF
⍝ POLYNOMIALS OVER THE CURRENT FINITE RING.       
 DERR FRTEST A                                    
 EPSILON←0                                        
 C←RXLEAD A
∇
==================================================
FUNCTION: FRXPROD
==================================================
∇ C←A FRXPROD B;⎕IO;D;RHO;I                          
⍝ COMPUTES THE ENTRY-BY-ENTRY PRODUCT OF TWO ARRAYS
⍝ OF POLYNOMIALS OVER THE FINITE RING.             
 EXPANDV                                           
 ⎕IO←0                                             
 D←((⍳¯1+⍴⍴A),0 ¯1+⍴⍴A)⍉B∘.×(¯1↑⍴A)⍴1              
 D←(A∘.×(¯1↑⍴B)⍴1)FRPROD D                         
 D←D,((⍴A),¯1+¯1↑⍴A)⍴0                             
 D←((⍴A)⍴-⍳¯1↑⍴A)⌽D                                
 RHO←⍴D                                            
 D←((×/¯2↓RHO),¯2↑RHO)⍴D                           
 C←(⍴D)[0 2]⍴0                                     
 I←¯1                                              
LOOP:→((⍴D)[1]=I←I+1)/END                          
 C←C FRSUM D[;I;]                                  
 →LOOP                                             
END:D←1⌈+/∨\⌽∨⌿0≠C                                 
 C←((¯2↓RHO),D)⍴((1↑⍴C),D)↑C
∇
==================================================
FUNCTION: FRXSUM
==================================================
∇ C←A FRXSUM B;M;D                                    
⍝ COMPUTES THE SUM OF TWO ARRAYS OF POLYNOMIALS OVER
⍝ THE FINITE RING.                                  
 EXPANDV                                            
 M←(⍴A)⌈⍴B                                          
 C←(M↑A)FRSUM M↑B                                   
 D←1⌈+/∨\⌽∨⌿((×/¯1↓⍴C),¯1↑⍴C)⍴C≠0                   
 C←((¯1↓⍴C),D)↑C
∇
==================================================
FUNCTION: GAUSSFACTOR
==================================================
∇ C←GAUSSFACTOR A;⎕IO;P;I;J;U;Q;NOTEST                 
⍝ PRODUCES A LIST OF GAUSSIAN PRIMES WHOSE PRODUCT   
⍝ IS AN ASSOCIATE OF THE NONZERO GAUSSIAN INTEGER  A.
⍝ NO RATIONAL PRIME IN THE NORM OF  A  MAY BE        
⍝ LARGER THAN 10000.                                 
 DERR∧/(,A=⌊A),(1≥⍴⍴A),(∨/,A≠0),(×/⍴A)ϵ1 2           
 C←0 2⍴0                                             
 ⎕IO←1                                               
 →(0=⍴P←SSORT ZFACTOR A+.×A←2↑A)/0                   
 DERR 10000>¯1↑P                                     
 Q←((2=P[1]),2)⍴1 1                                  
 Q←Q,[1]((3=4|P)/P),[1.5]0                           
 NOTEST←1                                            
 →(0=⍴P←(1=4|P)/P)/LOOP                              
 I←SFEL U=⌊U←(0⌈P∘.-(⍳⌊(¯1↑P)⋆0.5)⋆2)⋆0.5            
 Q←Q,[1]⍉(I,I),[0.5]J,-J←⌊(P-I×I)⋆0.5                
LOOP:→(0=⍴Q←(∧/0=Q GAUSSREM(⍴Q)⍴A)⌿Q)/END            
 C←C,[1]Q                                            
 A←⌊A CQUOT CPRODRED Q                               
 →LOOP                                               
END:C←C[⍋C[;2];]                                     
 C←C[⍋+/C⋆2;]
∇
==================================================
FUNCTION: GAUSSQUOT
==================================================
∇ C←A GAUSSQUOT B;EPSILON                     
⍝ COMPUTES ONE QUOTIENT OF  A  BY  B  IN THE
⍝ EUCLIDEAN DOMAIN OF GAUSSIAN INTEGERS.    
 EPSILON←0                                  
 C←⌊0.5+A CQUOT B
∇
==================================================
FUNCTION: GAUSSREM
==================================================
∇ C←A GAUSSREM B;EPSILON                               
⍝ COMPUTES ONE REMAINDER OF  B  DIVIDED BY  A  IN THE
⍝ EUCLIDEAN DOMAIN OF GAUSSIAN INTEGERS.             
 EPSILON←0                                           
 C←B CDIFF A CPROD B GAUSSQUOT A
∇
==================================================
FUNCTION: GCDV
==================================================
∇ D←GCDV A;M                   
⍝ EXERCISE 2.2.22            
 →(0<⍴A←(A≠0)/A←,A)/LOOP     
 →D←0                        
LOOP:A←(A≠0)/A←M,(M←⌊/A)|A←|A
 →(1<⍴A)/LOOP                
 D←(⍳0)⍴A
∇
==================================================
FUNCTION: GCDVX
==================================================
∇ D←GCDVX A;I;M;Q;X;S       
⍝ EXERCISE 2.2.23         
 →(0<⍴A←,A)/NONEMPTY      
 r←⍳0                     
 →D←0                     
NONEMPTY:r←(2⍴⍴A)⍴1,(⍴A)⍴0
 S←(A<0)/⍳⍴A              
 r[S;]←-r[S;]             
 A[S]←-A[S]               
LOOP:A←(X←A≠0)/A          
 r←X⌿r                    
 →(1≥⍴A)/DONE             
 I←A⍳M←⌊/A                
 Q←A ZQUOT M              
 A←M,M|A                  
 r←r[I;],[⎕IO]r-Q∘.×r[I;] 
 →LOOP                    
DONE:D←(⍳0)⍴A             
 r←,r
∇
==================================================
FUNCTION: GPALLORB
==================================================
∇ B←GPALLORB A;N;x;I;NOTEST;C                            
⍝ COMPUTES A SUMMARY OF THE ORBITS OF THE PERMUTATION  
⍝ GROUP GENERATED BY THE ROWS OF THE MATRIX  A.        
⍝ THE FIRST ROW OF  B  GIVES THE LENGTHS OF THE ORBITS.
⍝ THE SECOND ROW OF  B  GIVES REPRESENTATIVES.         
⍝ q[I]  IS THE FIRST POINT IN THE ORBIT CONTAINING  I. 
 DERR(GPTEST A)∧2=⍴⍴A                                  
 q←(N←¯1↑⍴A)⍴¯1                                        
 B←2 0⍴0                                               
 NOTEST←1                                              
LOOP:→((N+⎕IO)≤I←q⍳¯1)/0                               
 q[C←A GPORBIT I]←I                                    
 B←B,I,⍴C                                              
 →LOOP
∇
==================================================
FUNCTION: GPCYCIN
==================================================
∇ X←N GPCYCIN C;Y;I;D;U                                      
⍝ CONSTRUCTS THE VECTOR FORM OF THE PERMUTATION OF  ⍳N     
⍝ GIVEN AS A PRODUCT OF CYCLES IN THE CHARACTER VECTOR  C. 
⍝ THE CYCLES DO NOT NEED TO BE DISJOINT.  ORIGIN DEPENDENT.
 DERR(1=⍴N)∧N=⌊N←,N                                        
 X←⍳N                                                      
 C←(C≠' ')/C←,C                                            
⍝ GET THE NEXT CYCLE.                                      
LOOP:→(0=⍴C)/0                                             
 D←(I←(C⍳')')+1-⎕IO)↑C                                     
 C←I↓C                                                     
 DERR('('=1↑D)∧')'=¯1↑D                                    
 D←¯1↓1↓D                                                  
 D[(D=',')/⍳⍴D]←' '                                        
 DERR∧/Dϵ'0123456789 '                                     
 DERR(⍴U)=⍴SSORT U←,⍎D                                     
 DERR∧/U<N+⎕IO                                             
 Y←⍳N                                                      
 Y[U]←1⌽U                                                  
 X←Y[X]                                                    
 →LOOP
∇
==================================================
FUNCTION: GPCYCOUT
==================================================
∇ C←GPCYCOUT X;T;I;J                                
⍝ CONSTRUCTS THE CYCLE FORM OF THE PERMUTATION  X.
 DERR 1=⍴⍴X                                       
 DERR∧/X[⍋X]=⍳⍴X                                  
 C←''                                             
 T←(⍴X)⍴0                                         
⍝ FIND THE START OF THE NEXT CYCLE.               
LOOP1:→((⎕IO+⍴X)≤I←T⍳0)/0                         
 T[I]←1                                           
 C←C,'(',⍕J←I                                     
LOOP2:→(I=J←X[J])/CLOSE                           
 C←C,',',⍕J                                       
 T[J]←1                                           
 →LOOP2                                           
CLOSE:C←C,')'                                     
 →LOOP1
∇
==================================================
FUNCTION: GPINV
==================================================
∇ C←GPINV A;N;L;M                                  
⍝ COMPUTES THE INVERSES OF THE PERMUTATIONS IN A.
 →NOTEST/BEGIN                                   
 DERR GPTEST A                                   
BEGIN:C←(N←×/⍴A)⍴2                               
 L←⌊N÷M←¯1↑⍴A                                    
 C[(,A)+,⍉(M,L)⍴M×(⍳L)-⎕IO]←N⍴⍳M                 
 C←(⍴A)⍴C
∇
==================================================
FUNCTION: GPORBIT
==================================================
∇ C←A GPORBIT I;V                                       
⍝ COMPUTES A LIST  C  AND THE CHARACTERISTIC VECTOR  x
⍝ OF THE ORBIT CONTAINING  I  OF THE PERMUATION GROUP 
⍝ GENERATED BY THE ROWS OF THE MATRIX  A.             
 DERR(1=⍴I)∧(2=⍴⍴A)∧(∧/I=⌊I←,I)∧GPTEST A              
 x←(¯1↑⍴A)⍴0                                          
 x[C←V←I]←1                                           
LOOP:C←C,V←SSORT(∼x[V])/V←,A[;V]                      
 x[V]←1                                               
 →(0≠⍴V)/LOOP                                         
 C←SSORT C
∇
==================================================
FUNCTION: GPPROD
==================================================
∇ C←A GPPROD B;M;RHO;N;I                          
⍝ COMPUTES THE ELEMENT-BY-ELEMENT PRODUCT OF TWO
⍝ ARRAYS OF PERMUTATIONS (OR MAPS).             
 →NOTEST/BEGIN                                  
 DERR∧/(,A=⌊A),(,A≥⎕IO),,A<⎕IO+¯1↑⍴B            
 EXPANDV                                        
BEGIN:M←×/¯1↓RHO←⍴A                             
 N←¯1↑RHO                                       
 I←RHO⍴⍉(N,M)⍴N×(⍳M)-⎕IO                        
 C←(,B)[A+I]
∇
==================================================
FUNCTION: GPSGN
==================================================
∇ B←GPSGN A;C;D;N                                    
⍝ COMPUTES THE SIGNS OF THE PERMUTATIONS IN  A.    
 →NOTEST/BEGIN                                     
 DERR GPTEST A                                     
BEGIN:D←((⍳¯2+⍴⍴C),⎕IO+(⍴⍴C)-1 2)⍉C←A∘.×(N←¯1↑⍴A)⍴1
 B←¯1⋆+/+/(C>D)∧(⍴C)⍴(⍳N)∘.<⍳N
∇
==================================================
FUNCTION: GPSGP
==================================================
∇ H←GPSGP X;N;HP;V;VP                                    
⍝ COMPUTES THE PERMUTATION GROUP GENERATED BY THE      
⍝ ROWS OF THE MATRIX  X.  VALID FOR DEGREES AT MOST 12.
⍝ WORKSPACE FULL ERRORS ARE LIKELY FOR DEGREES OVER 7. 
 DERR(GPTEST X)∧(2=⍴⍴X)∧12≥¯1↑⍴X                       
 N←¯1↑⍴X                                               
 H←(N⍴N+1)⊤HP←SSORT(N+1)⊥(⍳N),V←X←⍉X                   
LOOP:HP←HP,VP←SSORT(∼VPϵHP)/VP←,(N+1)⊥X[V;]            
 H←H,V←(N⍴N+1)⊤VP                                      
 →(0≠⍴VP)/LOOP                                         
 H←⍉H
∇
==================================================
FUNCTION: GPSYMG
==================================================
∇ T←GPSYMG N;V                                       
⍝ LISTS THE ELEMENTS OF THE SYMMETRIC GROUP ON  ⍳N.
 DERR∧/(0≤N←''⍴N),(N=⌊N),1=⍴N←,N                   
 →(N>0)/GENERAL                                    
 T←1 0⍴0                                           
 →0                                                
GENERAL:T←((!N),N-1)⍴GPSYMG N-1                    
 V←,⍉((!N-1),N)⍴(⍳N)-⎕IO                           
 T←V⌽((-V)⌽T),N+⎕IO-1
∇
==================================================
FUNCTION: GPTEST
==================================================
∇ T←GPTEST A;M;N;Z                              
⍝ CHECKS THAT  A  IS AN ARRAY OF PERMUTATIONS.
 →(∼T←∧/(1≤⍴⍴A),,A=⌊A)/0                      
 →(∼T←(∧/,A≥⎕IO)∧∧/A<⎕IO+N←¯1↑⍴A)/0           
 Z←(×/⍴A)⍴0                                   
 Z[(,A)+,⍉(N,M)⍴N×(⍳M←×/¯1↓⍴A)-⎕IO]←1         
 T←∧/Z
∇
==================================================
FUNCTION: GTCHECK
==================================================
∇ T←GTCHECK G;⎕IO;E;N;M;I;GTABLE;GTIO;GTINV          
⍝ CHECKS WHETHER  G  IS A GROUP TABLE WITH IDENTITY
⍝ EQUAL TO THE INDEX ORIGIN.                       
⍝ IS  G  A SQUARE INTEGER MATRIX?                  
 →(∨/(2≠⍴⍴G),(≠/⍴G),,G≠⌊G)/NO                      
⍝ THE ORIGIN SHOULD BE SET EQUAL TO  ⌊/,G          
 →(∧/0 1≠E←⌊/,G)/NO                                
 GTIO←⎕IO←E                                        
⍝ CHECK CLOSURE.                                   
 →(∨/,G>M←¯1+⎕IO+N←1↑⍴G)/NO                        
⍝ ANY BINARY OPERATION ON  ⍳1  IS A GROUP.         
 →(N=1)/YES                                        
⍝ CHECK FOR TWO-SIDED IDENTITY.                    
 →(∨/(G[⎕IO;]≠⍳N),G[;⎕IO]≠⍳N)/NO                   
⍝ COPY  G  INTO  GTABLE FOR USE IN  GTSGP  AND     
⍝ SET  G  TO 1 TO SAVE SPACE.                      
 GTINIT G                                          
 G←1                                               
⍝ TRY TO FIND A GENERATING SET  U  WITH  N≥2⋆⍴U.   
 U←⍳0                                              
 X←⎕IO=⍳N                                          
LOOP1:→(M<I←X⍳0)/TEST                              
 →(N<2⋆⍴U←U,I)/NO                                  
 X[GTSGP U]←1                                      
 →LOOP1                                            
⍝ MAKE SURE ELEMENTS OF  U  HAVE LEFT INVERSES.    
TEST:→(∼∧/∨⌿GTABLE[;U]=⎕IO)/NO                     
⍝ CHECK ASSOCIATIVITY FOR TRIPLES WITH THIRD       
⍝ ELEMENT IN  U.                                   
 I←⎕IO-1                                           
LOOP2:→((⎕IO+⍴U)≤I←I+1)/YES                        
 →(∨/GTABLE[GTABLE;U[I]]≠GTABLE[;GTABLE[;U[I]]])/NO
 →LOOP2                                            
NO:→T←0                                            
YES:T←1
∇
==================================================
FUNCTION: GTCLEAR
==================================================
∇ GTCLEAR;I                                      
⍝ EXPUNGES THE VARIABLES DESCRIBING THE CURRENT
⍝ ABSTRACT GROUP.                              
 I←(⎕EX'GTABLE'),(⎕EX'GTIO'),⎕EX'GTINV'
∇
==================================================
FUNCTION: GTINIT
==================================================
∇ GTINIT A;⎕IO                             
⍝ INITIALIZES THE CURRENT ABSTRACT GROUP.
 GTABLE←A                                
 ⎕IO←GTIO←⌊/A[⎕IO←1;]                    
 GTINV←SFEL A=⎕IO
∇
==================================================
FUNCTION: GTLCON
==================================================
∇ B←GTLCON A;⎕IO;X                                        
⍝ COMPUTES THE CHARACTERISTIC MATRIX FOR LEFT CONGRUENCE
⍝ MODULO THE SUBGOUP OF THE CURRENT ABSTRACT            
⍝ GROUP LISTED IN  A.                                   
 ⎕IO←GTIO                                               
 DERR(1≤⍴A)∧GTTEST A←,A                                 
 X←(⍴GTINV)⍴0                                           
 X[A]←1                                                 
 DERR∧/,X[GTABLE[A;A]]                                  
 B←X[GTABLE[GTINV;]]
∇
==================================================
FUNCTION: GTPROD
==================================================
∇ C←A GTPROD B;⎕IO                                 
⍝ COMPUTES ENTRY-BY-ENTRY PRODUCTS IN THE CURRENT
⍝ ABSTRACT GROUP.                                
 ⎕IO←GTIO                                        
 →NOTEST/BEGIN                                   
 DERR(GTTEST A)∧GTTEST B                         
 EXPAND                                          
BEGIN:C←(,GTABLE)[B+(A-⎕IO)×⍴GTINV]
∇
==================================================
FUNCTION: GTRCON
==================================================
∇ B←GTRCON A;⎕IO;X                                         
⍝ COMPUTES THE CHARACTERISTIC MATRIX FOR RIGHT CONGRUENCE
⍝ MODULO THE SUBGROUP OF THE CURRENT ABSTRACT            
⍝ GROUP LISTED IN  A.                                    
 ⎕IO←GTIO                                                
 DERR(1≤⍴A)∧GTTEST A←,A                                  
 X←(⍴GTINV)⍴0                                            
 X[A]←1                                                  
 DERR∧/,X[GTABLE[A;A]]                                   
 B←X[GTABLE[;GTINV]]
∇
==================================================
FUNCTION: GTSGP
==================================================
∇ B←GTSGP A;⎕IO;V                                
⍝ COMPUTES THE SUBGROUP GENERATED BY  A  IN THE
⍝ CURRENT ABSTRACT GROUP.                      
 ⎕IO←GTIO                                      
 DERR GTTEST A                                 
 B←SSORT ⎕IO,V←,A                              
LOOP:B←B,V←SSORT(∼VϵB)/V←,GTABLE[V;A]          
 →(0≠⍴V)/LOOP                                  
 B←B[⍋B]
∇
==================================================
FUNCTION: GTTEST
==================================================
∇ T←GTTEST A                                   
⍝ CHECKS WHETHER  A  REPRESENTS AN ARRAY OVER
⍝ THE CURRENT ABSTRACT GROUP.                
 →(∼T←∧/,A=⌊A)/0                             
 T←(∧/,A≥GTIO)∧∧/,A<GTIO+⍴GTINV
∇
==================================================
FUNCTION: LCMV
==================================================
∇ M←LCMV A;N;A1;A2;D       
⍝ EXERCISE 2.2.24        
 →(0<⍴A←,A)/NONEMPTY     
 M←1                     
 →0                      
NONEMPTY:→(∧/A≠0)/NONZERO
 →M←0                    
NONZERO:→(1<⍴A)/LONG     
 M←(⍳0)⍴|A               
 →0                      
LONG:→(0=2|⍴A)/EVEN      
 A←A,1                   
EVEN:N←(⍴A)÷2            
 D←(A1←N↑A)ZGCD A2←N↓A   
 A←⌊(A1×A2)÷D            
 →NONZERO
∇
==================================================
FUNCTION: LISTFN
==================================================
∇ Z←LISTFN A;B;N;⎕IO                                       
 ⎕IO←1                                                   
 →(0=1↑⍴Z←A←⎕CR A)/0                                     
 N←¯1+⍴B←(A[;1]='⍝')∨B\(+/∨\B⌿Z)>+/∨\''''=(B←∨/Z←A=':')⌿A
 Z←N↑((N⌊9)⍴2),(0⌈90⌊N+9)⍴1                              
 Z←((' ',[1]'[',Z⌽(3 0⍕(N,1)⍴⍳N),']'),B⌽' ',A),[1]' '    
 Z[1,N+2;5]←'∇'
∇
==================================================
FUNCTION: LUCASLEHMER
==================================================
∇ T←LUCASLEHMER P;N;S;I                
⍝ EXERCISE 2.5.4                     
 →(1=⍴ZFACTOR P)/PRIME               
 'DOMAIN ERROR'                      
 →0                                  
PRIME:N←(,¯1)MPZSUM0(,2)MPZPOWER0 P  
 S←,4                                
 I←1                                 
LOOP:→(P≤I←I+1)/DONE                 
 S←N MPZREM0(,¯2)MPZSUM0 S MPZPROD0 S
 →LOOP                               
DONE:T←(1=⍴S)∧0=1↑S
∇
==================================================
FUNCTION: MAKEBIG
==================================================
∇ NUM MAKEBIG MAXP;⎕IO;N;I;J;C;n                 
⍝ CONSTRUCTS THE ARRAYS  BIGPRIMES  AND BIGINV,
⍝ WHICH ARE USED IN  MPZDET  AND WHICH ARE     
⍝ SYSTEM DEPENDENT.  BIGPRIMES  WILL CONSIST OF
⍝ THE  NUM  LARGEST PRIMES NOT EXCEEDING  MAXP,
⍝ WHICH SHOULD BE AN INTEGER WHOSE SQUARE IS   
⍝ REPRESENTABLE EXACTLY ON THE SYSTEM.         
 ⎕IO←1                                         
 N←0                                           
 BIGPRIMES←NUM⍴0                               
 MAXP←MAXP+1                                   
LOOP1:→(3>MAXP←MAXP-1)/ERROR                   
 →(1≠⍴ZFACTOR MAXP)/LOOP1                      
 BIGPRIMES[N←N+1]←MAXP                         
 →(NUM>N)/LOOP1                                
 BIGPRIMES←⌽BIGPRIMES                          
 BIGINV←NUM⍴0                                  
 I←0                                           
LOOP2:→(NUM<I←I+1)/0                           
 n←BIGPRIMES[I]                                
 J←0                                           
 C←1                                           
LOOP2A:→(I≤J←J+1)/NEXT                         
 C←C ZNPROD BIGPRIMES[J]                       
 →LOOP2A                                       
NEXT:BIGINV[I]←ZNINV C                         
 →LOOP2                                        
ERROR:'NUM IS TOO BIG OR'                      
 'MAXP IS TOO SMALL.'
∇
==================================================
FUNCTION: MPZDET
==================================================
∇ D←MPZDET A;⎕IO;E;N;n;F;G;P;I;q;N2                     
⍝ MULTIPLE PRECISION DETERMINANT OF A SINGLE PRECISION
⍝ INTEGER MATRIX A LA CABAY AND LAM.                  
 DERR∧/(2=⍴⍴A),(=/⍴A),,A=⌊A                           
 ⎕IO←1                                                
 E←(⍟2)++/⍟(+/A×A)⋆0.5                                
 DERR(⍴BIGPRIMES)≥N←⌈E÷⍟BIGPRIMES[1]                  
 N2←⌊0.5×n←BIGPRIMES[1]                               
 D←,(n|N2+ZNDET A)-N2                                 
 P←,1                                                 
 I←1                                                  
LOOP:→(N<I←I+1)/END                                   
 N2←⌊0.5×n←BIGPRIMES[I]                               
 F←ZNDET A                                            
 G←(n|N2+BIGINV[I]×F-1000000⊥(,n)MPZREM0 D)-N2        
 P←P MPZPROD0,BIGPRIMES[I-1]                          
 D←D MPZSUM0 P MPZPROD0,G                             
 →LOOP                                                
END:D←MPZFORM D
∇
==================================================
FUNCTION: MPZDIFF
==================================================
∇ Z←X MPZDIFF Y                                      
⍝ COMPUTES THE DIFFERENCE OF TWO MULTIPLE PRECISION
⍝ INTEGERS REPRESENTED AS CHARACTER VECTORS.       
 Z←MPZFORM(MPZUNF X)MPZSUM0-MPZUNF Y
∇
==================================================
FUNCTION: MPZFORM
==================================================
∇ X←MPZFORM A                                     
⍝ CONVERTS A VECTOR OF DIGITS TO THE BASE 1E6 TO
⍝ A VECTOR OF CHARACTERS.                       
 X←,((⍴A),¯6)↑⍕((⍴A),1)⍴⌊|A←,A                  
 X[(X=' ')/⍳⍴X]←'0'                             
 X←((¯1=×1↑A)⍴'¯'),((('0'≠¯1↓X)⍳1)-⎕IO)↓X
∇
==================================================
FUNCTION: MPZGCD
==================================================
∇ Z←X MPZGCD Y                                 
⍝ COMPUTES THE GCD OF TWO INTEGERS GIVEN BY  
⍝ CHARACTER VECTORS OF DIGITS TO THE BASE 10.
 Z←MPZFORM(MPZUNF X)MPZGCD0 MPZUNF Y
∇
==================================================
FUNCTION: MPZGCD0
==================================================
∇ C←A MPZGCD0 B;q                         
⍝ COMPUTES THE GCD OF TWO INTEGERS GIVEN
⍝ BY VECTORS OF DIGITS TO THE BASE 1E6. 
 A←|MPZNRMLZ A                          
 C←|MPZNRMLZ B                          
LOOP:→(0=1↑A)/0                         
 B←A MPZREM0 C                          
 C←A                                    
 A←B                                    
 →LOOP
∇
==================================================
FUNCTION: MPZMAG
==================================================
∇ B←MPZMAG A;N                               
⍝ COMPUTES THE ABSOLUTE VALUE OF AN INTEGER
⍝ GIVEN BY A CHARACTER VECTOR OF DIGITS TO 
⍝ THE BASE 10.                             
 DERR(1≥⍴⍴A)∧∧/,Aϵ'0123456789+¯'           
 →(∼(1↑A←,A)ϵ'+¯')/NOSIGN                  
 A←1↓A                                     
NOSIGN:N←+/∧\A='0'                         
 →(0<⍴B←N↓A)/0                             
 B←,'0'
∇
==================================================
FUNCTION: MPZMAG0
==================================================
∇ B←MPZMAG0 A                                 
⍝ COMPUTES THE MAGNITUDE OF AN INTEGER GIVEN
⍝ BY A VECTOR OF DIGITS TO THE BASE 1E6.    
 B←|MPZNRMLZ A
∇
==================================================
FUNCTION: MPZNEG
==================================================
∇ B←MPZNEG A;⎕IO;I;C                               
⍝ COMPUTES THE NEGATIVE OF AN INTEGER GIVEN      
⍝ BY A CHARACTER VECTOR OF DIGITS TO THE BASE 10.
 ⎕IO←0                                           
 DERR(1≥⍴⍴A)∧' '=1↑0↑,A                          
 I←(C←1↑B←,A)ϵ'+¯'                               
 B←I↓B                                           
 DERR∧/Bϵ'0123456789'                            
 B←(+/∧\'0'=¯1↓B)↓B                              
 →((C='¯')∨'0'=1↑B)/0                            
 B←'¯',B
∇
==================================================
FUNCTION: MPZNRMLZ
==================================================
∇ B←MPZNRMLZ A;SIGN;S                             
⍝ NORMALIZES A VECTOR OF DIGITS TO THE BASE 1E6.
 DERR∧/(1≥⍴⍴A),B=⌊B←,A                          
 SIGN←1                                         
LOOP:→(0=⍴B←(((B≠0)⍳1)-⎕IO)↓B)/ZERO             
 B←⌊B×S←×1↑B                                    
 SIGN←S×SIGN                                    
 →(∧/(B<1000000),B≥0)/END                       
 B←(S,0)+0,B-1000000×S←⌊B÷1000000               
 →LOOP                                          
ZERO:→B←,0                                      
END:B←SIGN×B
∇
==================================================
FUNCTION: MPZPOWER
==================================================
∇ Z←X MPZPOWER N                                     
⍝ COMPUTES THE N-TH POWER OF THE MULTIPLE PRECISION
⍝ INTEGER WITH CHARACTER VECTOR  X.  N  IS AN      
⍝ ORDINARY INTEGER.                                
 Z←MPZFORM(MPZUNF X)MPZPOWER0 N
∇
==================================================
FUNCTION: MPZPOWER0
==================================================
∇ B←A MPZPOWER0 N                             
⍝ RAISES A VECTOR OF DIGITS TO BASE 1E6 TO  
⍝ THE POWER N, WHICH IS AN ORDINARY INTEGER.
 DERR(N=⌊N)∧N≥0                             
 A←MPZNRMLZ A                               
 B←,1                                       
LOOP:→(N=0)/0                               
 →(0=2|N)/EVEN                              
 B←B MPZPROD0 A                             
EVEN:A←A MPZPROD0 A                         
 N←⌊N÷2                                     
 →LOOP
∇
==================================================
FUNCTION: MPZPROD
==================================================
∇ Z←X MPZPROD Y                                   
⍝ MULTIPLE PRECISION PRODUCT OF INTEGERS GIVEN  
⍝ BY CHARACTER VECTORS OF DIGITS TO THE BASE 10.
 Z←MPZFORM(MPZUNF X)MPZPROD0 MPZUNF Y
∇
==================================================
FUNCTION: MPZPROD0
==================================================
∇ C←A MPZPROD0 B;⎕IO;U                              
⍝ COMPUTES THE PRODUCT OF TWO VECTORS OF DIGITS TO
⍝ THE BASE 1E6.                                   
 ⎕IO←0                                            
 U←(A←,A)∘.×,B                                    
 C←MPZNRMLZ+⌿(-⍳⍴A)⌽U,(0 ¯1+2⍴⍴A)⍴0
∇
==================================================
FUNCTION: MPZREM
==================================================
∇ Z←X MPZREM Y                                        
⍝ COMPUTES THE REMAINDER WHEN THE MULTIPLE PRECISION
⍝ INTEGER  Y  IS DIVIDED BY THE MULTIPLE PRECISION  
⍝ INTEGER  X.  THE INTEGER QUOTIENT IS SAVED IN THE 
⍝ GLOBAL VARIABLE  q.  HERE  X  AND  Y  ARE         
⍝ CHARACTER VECTORS OF DIGITS TO THE BASE 10.       
 Z←MPZFORM(MPZUNF X)MPZREM0 MPZUNF Y                
 q←MPZFORM q
∇
==================================================
FUNCTION: MPZREM0
==================================================
∇ C←A MPZREM0 B;⎕IO;I;L;M;N;Q;R;SA;SC;T                  
⍝ COMPUTES MULTIPLE PRECISION REMAINDER USING VECTORS  
⍝ OF DIGITS TO THE BASE 1E6.  THE QUOTIENT IS SAVED    
⍝ IN THE GLOBAL VARIABLE  q.                           
 q←,⎕IO←0                                              
 C←MPZNRMLZ B                                          
 →(0=SA←×1↑A←MPZNRMLZ A)/0                             
 A←|A                                                  
LOOP:→(((⍴C)<⍴A)∧0>SC←×1↑C)/NEG                        
 →((⍴C)>⍴A)/DIVIDE                                     
 →(0>SC)/DIVIDE                                        
 →((⍴C)<⍴A)/0                                          
 →((⍴A)=I←(A≠C)⍳1)/DIVIDE                              
 →(A[I]>C[I])/0                                        
DIVIDE:N←⌊10⍟Q←(1000000⊥|(M←3⌊⍴C)↑C)÷1000000⊥(L←3⌊⍴A)↑A
 →(12>T←N+6×((⍴C)-M)-(⍴A)-L)/SMALL                     
 Q←⌊Q×10⋆T-N+6×R←¯2+⌊T÷6                               
 Q←(SA×SC×,(3⍴1000000)⊤Q),R⍴0                          
 →ADJUST                                               
SMALL:Q←⌊SA×SC×Q×10⋆T-N                                
 Q←(×Q)×((1+⌊10⍟|Q)⍴1000000)⊤|Q                        
ADJUST:q←q MPZSUM0 Q                                   
 C←C MPZSUM0(-SA)×Q MPZPROD0 A                         
 →LOOP                                                 
NEG:C←C MPZSUM0 A                                      
 q←q MPZSUM0-SA
∇
==================================================
FUNCTION: MPZSGN
==================================================
∇ T←MPZSGN A                                             
⍝ COMPUTES THE SIGNUM OF A MULTIPLE PRECISION INTEGER  
⍝ GIVEN BY A CHARACTER VECTOR OF DIGITS TO THE BASE 10.
 DERR∧/(1≥⍴⍴A),,Aϵ'0123456789+¯'                       
 →('¯'≠1↑A←,A)/NONNEG                                  
 T←¯1                                                  
 →0                                                    
NONNEG:→(∧/Aϵ'0+')/ZERO                                
 T←1                                                   
 →0                                                    
ZERO:T←0
∇
==================================================
FUNCTION: MPZSUM
==================================================
∇ Z←X MPZSUM Y                                         
⍝ COMPUTES THE SUM OF TWO MULTIPLE PRECISION INTEGERS
⍝ IN CHARACTER FORM.                                 
 Z←MPZFORM(MPZUNF X)MPZSUM0 MPZUNF Y
∇
==================================================
FUNCTION: MPZSUM0
==================================================
∇ C←A MPZSUM0 B;M                      
⍝ ADDS VECTORS OF DIGITS TO BASE 1E6.
 M←-(⍴A←,A)⌈⍴B←,B                    
 C←MPZNRMLZ(M↑A)+M↑B
∇
==================================================
FUNCTION: MPZUNF
==================================================
∇ A←MPZUNF X;⎕IO;M;SIGN                                  
⍝ CONVERTS THE CHARACTER VECTOR OF A MULTIPLE PRECISION
⍝ INTEGER INTO A VECTOR OF DIGITS TO THE BASE 1E6.     
 ⎕IO←0                                                 
 M←∨/'+¯'=1↑X←,X                                       
 SIGN←1↑M↑X                                            
 DERR∧/(X←M↓X)ϵ'0123456789'                            
 A←,⍎((7×M)⍴0 1 1 1 1 1 1)\(¯6×M←⌈(⍴X)÷6)↑X            
 A←(¯1⋆SIGN='¯')×A
∇
==================================================
FUNCTION: NOCOMS
==================================================
∇ NOCOMS;⎕IO;NL;I;X;A                      
⍝ DELETES ALL COMMENTS FROM ALL FUNCTIONS
⍝ EXCEPT ITSELF.                         
 ⎕IO←1                                   
 NL←⎕NL 3                                
 I←0                                     
LOOP:→((1↑⍴NL)<I←I+1)/0                  
 →(∧/'NOCOMS'=6↑X←NL[I;])/LOOP           
 →(0=1↑⍴A←⎕CR X)/LOOP                    
 A←(A[;1]≠'⍝')⌿A                         
 B←⎕FX A                                 
 →LOOP
∇
==================================================
FUNCTION: PHI
==================================================
∇ M←PHI N;P;Q;E       
⍝ EXERCISE 3.6.17   
 P←SSORT Q←ZFACTOR N
 E←+/P∘.=Q          
 M←×/(P⋆E-1),P-1
∇
==================================================
FUNCTION: POWERR
==================================================
∇ Y←X POWERR N          
⍝ EXERCISE 3.1.27     
 →(N>0)/POS           
 Y←1                  
 →0                   
POS:Y←Y×Y←X POWERR⌊N÷2
 →(0=2|N)/0           
 Y←X×Y
∇
==================================================
FUNCTION: QDIFF
==================================================
∇ C←A QDIFF B                                      
⍝ COMPUTES THE DIFFERENCE OF TWO RATIONAL ARRAYS.
 C←A QSUM QNEG B
∇
==================================================
FUNCTION: QINV
==================================================
∇ B←QINV A;D                                    
⍝ COMPUTES THE RECIPROCAL OF A RATIONAL ARRAY.
 →NOTEST/BEGIN                                
 A←QNRMLZ A                                   
 DERR∧/0≠,1 0/A                               
BEGIN:B←(⌽A)×D,D←×1 0/A
∇
==================================================
FUNCTION: QMATPROD
==================================================
∇ C←A QMATPROD B;⎕IO;X;AX;BX;RR;NOTEST;RA;RB           
⍝ COMPUTES THE MATRIX PRODUCT OF TWO NONSCALAR ARRAYS
⍝ OF RATIONAL NUMBERS.                               
 ⎕IO←1                                               
 NOTEST←0                                            
 A←QNRMLZ A                                          
 B←QNRMLZ B                                          
 DERR∧/2≤(⍴⍴A),⍴⍴B                                   
 DERR(⍴A)[¯1+⍴⍴A]=1↑⍴B                               
 C←((RA←¯2↓⍴A),(RB←¯1↓1↓⍴B),2)⍴0 1                   
 X←1=⍳1↑⍴B                                           
 RR←((⍴RA)+⍳⍴RB),(⍳⍴RA),⍴⍴C                          
 NOTEST←1                                            
LOOP:AX←RR⍉(RB,RA,2)⍴X/[¯1+⍴⍴A]A                     
 BX←(⍴C)⍴X⌿B                                         
 C←C QSUM AX QPROD BX                                
 →(∼1↑X←¯1⌽X)/LOOP
∇
==================================================
FUNCTION: QNEG
==================================================
∇ B←QNEG A                                    
⍝ COMPUTES THE NEGATIVE OF A RATIONAL ARRAY.
 →NOTEST/BEGIN                              
 A←QNRMLZ A                                 
BEGIN:B←A×(⍴A)⍴¯1 1
∇
==================================================
FUNCTION: QNRMLZ
==================================================
∇ B←QNRMLZ A;D;RHO                                      
⍝ COMPUTES THE STANDARD REPRESENTATION OF AN ARRAY OF 
⍝ RATIONAL NUMBERS EXPRESSED AS QUOTIENTS OF INTEGERS.
⍝ FOR SCALARS AND ARRAYS OF VECTORS OF LENGTH 1 A     
⍝ DENOMINATOR OF 1 IS ADDED.                          
 →NOTEST/BEGIN                                        
 DERR QTEST A                                         
BEGIN:→((0=⍴⍴B)∨1=¯1↑⍴B←A)/ADDDEN                     
 RHO←¯1↓⍴A                                            
 D←(((RHO,1)↑A)ZGCD0 D)××D←(RHO,¯1)↑A                 
 B←⌊A÷D,D                                             
 →0                                                   
ADDDEN:B←A,1
∇
==================================================
FUNCTION: QPOWER
==================================================
∇ C←A QPOWER B;RHO;RC;I;J;NOTEST               
⍝ COMPUTES THE B-TH POWER OF THE RATIONAL    
⍝ ARRAY  A  USING THE BINARY POWER ALGORITHM.
 NOTEST←0                                    
 A←QNRMLZ A                                  
 DERR∧/(,B=⌊B),,B≥0                          
 B←((⍴B),1)⍴B                                
 EXPANDV                                     
 RC←(×/¯1↓RHO←⍴A),2                          
 A←RC⍴A                                      
 C←RC⍴1 1                                    
 I←(B>0)/⍳⍴B←,B                              
 NOTEST←1                                    
LOOP:C[J;]←C[J;]QPROD A[J←(2|B[I])/I;]       
 →(0=⍴I←(B[I]≥2)/I)/END                      
 A[I;]←A[I;]QPROD A[I;]                      
 B[I]←⌊B[I]÷2                                
 →LOOP                                       
END:C←RHO⍴C
∇
==================================================
FUNCTION: QPROD
==================================================
∇ C←A QPROD B;NT                                
⍝ COMPUTES THE PRODUCT OF TWO RATIONAL ARRAYS.
 →NOTEST/BEGIN                                
 A←QNRMLZ A                                   
 B←QNRMLZ B                                   
 EXPANDV                                      
BEGIN:NT←NOTEST                               
 NOTEST←1                                     
 C←QNRMLZ A×B                                 
 NOTEST←NT
∇
==================================================
FUNCTION: QQUOT
==================================================
∇ C←A QQUOT B                                    
⍝ COMPUTES THE QUOTIENT OF TWO RATIONAL ARRAYS.
 C←A QPROD QINV B
∇
==================================================
FUNCTION: QSUM
==================================================
∇ C←A QSUM B;RA;RB;AN;AD;BN;BD;NT           
⍝ COMPUTES THE SUM OF TWO RATIONAL ARRAYS.
 →NOTEST/BEGIN                            
 A←QNRMLZ A                               
 B←QNRMLZ B                               
 EXPANDV                                  
BEGIN:RA←¯1↓⍴A                            
 RB←¯1↓⍴B                                 
 AN←(RA,1)↑A                              
 AD←(RA,¯1)↑A                             
 BN←(RB,1)↑B                              
 BD←(RB,¯1)↑B                             
 NT←NOTEST                                
 NOTEST←1                                 
 C←QNRMLZ((AN×BD)+AD×BN),AD×BD            
 NOTEST←NT
∇
==================================================
FUNCTION: QTEST
==================================================
∇ T←QTEST A                                     
⍝ CHECKS WHETHER  A  REPRESENTS AN ARRAY      
⍝ OF RATIONAL NUMBERS.                        
 →(∼T←(∧/,A=⌊A)∧(0=⍴⍴A)∨(0<⍴⍴A)∧∨/1 2=¯1↑⍴A)/0
 →((0=⍴⍴A)∨1=¯1↑⍴A)/0                         
 T←∧/0≠,0 1/A
∇
==================================================
FUNCTION: RACLEAR
==================================================
∇ RACLEAR;I                                      
⍝ EXPUNGES THE ARRAY OF STRUCTURE CONSTANTS FOR
⍝ THE CURRENT R-ALGEBRA.                       
 I←⎕EX'RSC'
∇
==================================================
FUNCTION: RADIFF
==================================================
∇ C←A RADIFF B                                    
⍝ COMPUTES DIFFERENCES IN THE CURRENT R-ALGEBRA.
 C←A RASUM-B
∇
==================================================
FUNCTION: RAINIT
==================================================
∇ RAINIT A                                      
⍝ INITIALIZED THE ARRAY OF STRUCTURE CONSTANTS
⍝ FOR THE CURRENT R-ALGEBRA.                  
 DERR∧/(3=⍴⍴A),(1↓⍴A)=¯1↓⍴A                   
 RSC←A
∇
==================================================
FUNCTION: RANEG
==================================================
∇ C←RANEG A                                     
⍝ COMPUTES NEGATIVES IN THE CURRENT R-ALGEBRA.
 C←RANRMLZ-A
∇
==================================================
FUNCTION: RANRMLZ
==================================================
∇ C←RANRMLZ A;⎕IO                                  
⍝ RETURNS THE STANDARD REPRESENTATION OF AN ARRAY
⍝ OVER THE THE CURRENT R-ALGEBRA.  SCALARS AND   
⍝ VECTORS OF LENGTH 1 ARE PADDED WITH ZEROS.     
 ⎕IO←1                                           
 DERR(0=⍴⍴A)∨(1=¯1↑⍴A)∨(1↑⍴RSC)=¯1↑⍴A            
 C←((⍴A),⍳0=⍴⍴A)⍴A                               
 →((1↑⍴RSC)=¯1↑⍴C)/0                             
 C←((¯1↓⍴C),1↑⍴RSC)↑C
∇
==================================================
FUNCTION: RAPOWER
==================================================
∇ C←A RAPOWER B;R;RHO;I;J;M                      
⍝ COMPUTES THE B-TH POWER OF  A  IN THE CURRENT
⍝ R-ALGEBRA.                                   
 DERR∧/(,B=⌊B),,B≥0                            
 A←RANRMLZ A                                   
 B←((⍴B),1)⍴B                                  
 EXPANDV                                       
 R←×/¯1↓RHO←⍴A                                 
 A←(R,M←¯1↑⍴A)⍴A                               
 C←(⍴A)⍴M↑1                                    
 I←(B>0)/⍳⍴B←,B                                
LOOP:C[J;]←C[J;]RAPROD A[J←(2|B[I])/I;]        
 →(0=⍴I←(B[I]≥2)/I)/END                        
 A[I;]←A[I;]RAPROD A[I;]                       
 B[I]←⌊B[I]÷2                                  
 →LOOP                                         
END:C←RHO⍴C
∇
==================================================
FUNCTION: RAPROD
==================================================
∇ C←A RAPROD B;⎕IO;R;RHO;M                     
⍝ COMPUTES PRODUCTS IN THE CURRENT R-ALGEBRA.
 A←RANRMLZ A                                 
 B←RANRMLZ B                                 
 EXPANDV                                     
 R←×/¯1↓RHO←⍴A                               
 ⎕IO←0                                       
 M←¯1↑⍴RSC                                   
 A←(R,M×M)⍴2 0 1⍉(M,R,M)⍴A                   
 B←(R,M×M)⍴1 0 2⍉(M,R,M)⍴B                   
 C←A×B                                       
 C←RHO⍴C+.×((M×M),M)⍴RSC
∇
==================================================
FUNCTION: RASUM
==================================================
∇ C←A RASUM B                             
⍝ COMPUTE SUMS IN THE CURRENT R-ALGEBRA.
 A←RANRMLZ A                            
 B←RANRMLZ B                            
 EXPANDV                                
 C←A+B
∇
==================================================
FUNCTION: RDET
==================================================
∇ D←RDET A;⎕IO;K;M;I;J;X;Y                         
⍝ COMPUTES AN APPROXIMATION TO THE DETERMINANT OF
⍝ THE REAL MATRIX  A.                            
 DERR(2=⍴⍴A)∧=/⍴A                                
 D←⎕IO←1                                         
LOOP:→(0=K←1↑⍴A)/0                               
 A←A×(|A)≥EPSILON×M←⌈/,|A                        
 →(M=0)/ZERO                                     
 I←(⌈/|A)⍳M                                      
 J←(|A[I;])⍳M                                    
 D←D×A[I;J]×¯1⋆I+J                               
 X←A[I;]÷A[I;J]                                  
 A←(I≠⍳K)⌿A                                      
 A←(J≠⍳K)/A-A[;J]∘.×X                            
 →LOOP                                           
ZERO:D←0
∇
==================================================
FUNCTION: RLSYS
==================================================
∇ C←A RLSYS B;T;X;r;v                                   
⍝ SOLVES LINEAR SYSTEMS OVER  R.  PRODUCES AN ARRAY  C
⍝ SUCH THAT  A+.×C  IS  B  AND A MATRIX  w  WHOSE     
⍝ ROWS SPAN THE SOLUTION SPACE OF THE CORRESPONDING   
⍝ HOMOGENEOUS SYSTEM.                                 
 DERR∧/(2=⍴⍴A),(1≤⍴⍴B),(1↑⍴A)=1↑⍴B                    
 A←RROWREDUCE A                                       
 B←B×(|B)≥EPSILON×⌈/(,|A),,|B←r+.×B                   
 DERR∧/,0=((⍴v),(¯1+⍴⍴B)⍴0)↓B                         
 X←(∼T←(¯1↑⍴A)SCHV v)/⍳¯1↑⍴A                          
 w←((⍴X),⍴T)⍴0                                        
 w[;X]←X∘.=X                                          
 w[;v]←⍉-A[⍳⍴v;X]                                     
 C←T⍀((⍴v),1↓⍴B)↑B
∇
==================================================
FUNCTION: RROWREDUCE
==================================================
∇ B←RROWREDUCE A;IO;I;J;K;L;M;F;X                   
⍝ ROW REDUCES THE REAL MATRIX  B.  PRODUCES  r, AN
⍝ INVERTIBLE REAL MATRIX SUCH THAT  B  IS  r+.×A. 
⍝ THE VECTOR  v  LISTS THE COLUMNS CONTAINING THE 
⍝ CORNER ENTRIES OF  B.                           
 DERR 2=⍴⍴B←A×(|A)≥EPSILON×⌈/,|A                  
 IO←⎕IO                                           
 ⎕IO←1                                            
 L←¯1↑⍴B                                          
 r←(K,K)⍴1,(K←1↑⍴B)⍴0                             
 v←⍳I←J←0                                         
LOOP:→((J≥K)∨L<I←I+1)/END                         
 →(0=M←⌈/C←|J↓B[;I])/LOOP                         
 v←v,I                                            
 X←J+C⍳M                                          
 B[J,X;]←B[X,J←J+1;]                              
 r[J,X;]←r[X,J;]                                  
 B[J;]←B[J;]×M←÷B[J;I]                            
 r[J;]←r[J;]×M                                    
 F←(J≠⍳K)×B[;I]                                   
 B←B×(|B)≥EPSILON×⌈/,|B←B-F∘.×B[J;]               
 r←r-F∘.×r[J;]                                    
 →LOOP                                            
END:v←v-1-⎕IO←IO                                  
 r←r×(|r)≥EPSILON×⌈/,|r
∇
==================================================
FUNCTION: RXDEGREE
==================================================
∇ B←RXDEGREE A                                  
⍝ COMPUTES THE ARRAY OF DEGREES OF AN ARRAY OF
⍝ REAL POLYNOMIALS.                           
 →(0<⍴⍴A)/BEGIN                               
 A←,A                                         
BEGIN:B←¯1++/∨\⌽0≠A×(|A)≥EPSILON×⌈/,|A
∇
==================================================
FUNCTION: RXDET
==================================================
∇ D←RXDET A;⎕IO;V;M;X;J;W;Q;R;S;U;DEG;a;NOTEST
⍝ COMPUTES THE DETERMINANT OF A MATRIX      
⍝ OF REAL POLYNOMIALS.                      
 DERR(3=⍴⍴A)∧=/2↑⍴A                         
 D←,⎕IO←1                                   
 →(0=1↑⍴A)/0                                
 A←A×(|A)≥EPSILON×⌈/,|A                     
 NOTEST←1                                   
LOOP:→(1=1↑⍴A)/END                          
BACK:→(∧/¯1=DEG←RXDEGREE V←A[;1;])/ZERO     
 M←⌊/(DEG>¯1)/DEG                           
 X←(M=DEG)/⍳⍴DEG                            
 J←X[(|V[X;M+1])⍳⌈/|V[X;M+1]]               
 →(J=1)/OK                                  
 A[1,J;;]←A[J,1;;]                          
 D←-D                                       
OK:→(∧/,0=W←1 0↓A[;1;])/ENDLP               
 Q←(-1 0+⍴U)↑U←W RXQUOT A[1;1;]             
 R←TRAV((2↑⍴A),¯1↑⍴Q)⍴Q                     
 S←(⍴A)⍴A[1;;]                              
 A←A RXDIFF R RXPROD S                      
 →BACK                                      
ENDLP:D←D RXPROD A[1;1;]                    
 A←1 1 0↓A                                  
 →LOOP                                      
ZERO:D←,0                                   
 →0                                         
END:D←D RXPROD A[1;1;]
∇
==================================================
FUNCTION: RXDIFF
==================================================
∇ C←A RXDIFF B                                                
⍝ COMPUTES THE DIFFERENCE OF TWO ARRAYS OF REAL POLYNOMIALS.
 C←A RXSUM-B
∇
==================================================
FUNCTION: RXEVAL
==================================================
∇ Y←A RXEVAL B;⎕IO                              
⍝ EVALUATES THE REAL POLYNOMIALS IN  A  AT  B.
 ⎕IO←0                                        
 B←((⍴B),1)⍴B                                 
 EXPANDV                                      
 B←(¯1↓⍴B)⍴B                                  
 Y←+/A×B∘.⋆⍳¯1↑⍴A                             
 Y←Y×(|Y)≥EPSILON×⌈/,|Y
∇
==================================================
FUNCTION: RXFACTOR
==================================================
∇ G←RXFACTOR 
      F;⎕IO;D;TOL;N;GCD;DF;r;s;H;S;ADDH;CENT;DEL;DER;DH;DR;MAX;NEWR;a;A;CLOSE;CN
      T;I;ND;SQ;S2;U;VAL;X
⍝ ATTEMPTS 
      TO PRODUCE A LIST OF MONIC REAL                                           
                          
⍝ IRREDUCIB
      LE POLYNOMIALS WHOSE PRODUCT IS THE                                       
                          
⍝ MONIC ASS
      OCIATE OF A GIVEN POLYNOMIAL.                                             
                          
 ⎕IO←0     
                                                                                
                          
 DERR∧/(1=⍴
      ⍴F),,0<D←RXDEGREE F                                                       
                          
 TOL←EPSILO
      N×⌈/,|F←((D+1)↑F)÷F[D]                                                    
                          
 SQ←4 2⍴1 1
       ¯1 1 ¯1 ¯1 1 ¯1                                                          
                          
 N←+/∧\0=F 
                                                                                
                          
 G←(N,3)⍴0 
      1 0                                                                       
                          
AGAIN:GCD←F
       RXGCD DF←1↓F×⍳⍴F←N↓F                                                     
                          
 DERR∧/TOL≥
      |GCD RXDIFF(F RXPROD r)RXSUM DF RXPROD s                                  
                          
 →(2<D←⍴H←F
       RXQUOT GCD)/NONLIN                                                       
                          
 CENT←1 2⍴2
      ↑-H[0]÷H[1]                                                               
                          
 →CLEANUP  
                                                                                
                          
NONLIN:CENT
      ←(2 2↑SQ)×S←0.5×⌈/(⌽D×|¯1↓H)⋆÷1↓⍳D                                        
                          
 ADDH←|1↓DH
      ×⍳⍴DH←1↓H×⍳⍴H                                                             
                          
 DH←DH,0   
                                                                                
                          
 CLOSE←CNT←
      0                                                                         
                          
LOOP:→(15<C
      NT←CNT+1)/CLEANUP                                                         
                          
 DER←VAL←(⍴
      CENT)⍴0                                                                   
                          
 I←D       
                                                                                
                          
EVAL:→(0>I←
      I-1)/DONE                                                                 
                          
 VAL←((⍴VAL
      )⍴H[I],0)+(-/CENT×VAL),[0.5]+/CENT×⌽VAL                                   
                          
 DER←((⍴DER
      )⍴DH[I],0)+(-/CENT×DER),[0.5]+/CENT×⌽DER                                  
                          
 →EVAL     
                                                                                
                          
DONE:X←∼TOL
      ≥DR←(ND←+/DER×DER)⋆0.5                                                    
                          
 DEL←(X⌿DER
      ×(⍴DER)⍴1 ¯1)÷ND,[0.5]ND←X/ND                                             
                          
 DEL←(-/VAL
      ×DEL),[0.5]+/DEL×⌽VAL←X⌿VAL                                               
                          
 →CLOSE/NEW
      TON                                                                       
                          
 MAX←(S2←S×
      1.415)+(+/X⌿CENT×CENT)⋆0.5                                                
                          
 MAX←(MAX∘.
      ⋆⍳⍴ADDH)+.×ADDH                                                           
                          
 NEWR←MAX×S
      ×S÷X/DR                                                                   
                          
 X←(∼X)∨X\(
      NEWR+S2)≥(+/DEL×DEL)⋆0.5                                                  
                          
 CENT←(4 1×
      ⍴CENT)⍴0 2 1 2⍉(CENT←X⌿CENT)∘.+SQ×S←S÷2                                   
                          
 CLOSE←(8≤C
      NT)∨(1↑⍴CENT)≤1↑⍴DER                                                      
                          
 →LOOP     
                                                                                
                          
NEWTON:CENT
      ←(X⌿CENT)-DEL                                                             
                          
 →(∧/,TOL≥|
      VAL)/CLEANUP                                                              
                          
 →LOOP     
                                                                                
                          
CLEANUP:CEN
      T←(CENT[;1]≥0)⌿CENT                                                       
                          
 D←⍴F      
                                                                                
                          
 I←¯1      
                                                                                
                          
NEXT:→((1↑⍴
      CENT)≤I←I+1)/END                                                          
                          
 A←CENT[I;]
                                                                                
                          
 →(A[1]≠0)/
      COMPLEX                                                                   
                          
 U←(-A[0]),
      1                                                                         
                          
 →CHECK    
                                                                                
                          
COMPLEX:U←(
      +/A×A),(-2×A[0]),1                                                        
                          
CHECK:→(∼∧/
      TOL≥|U RXREM F)/NEXT                                                      
                          
 G←G,[0]3↑U
                                                                                
                          
 F←F RXQUOT
       U                                                                        
                          
 →CHECK    
                                                                                
                          
END:DERR D>
      ⍴F                                                                        
                          
 →(1<⍴F)/AG
      AIN                                                                       
                          
 G←G×∼(|G)≤
      EPSILON×⌈/,|G
∇
==================================================
FUNCTION: RXFCLEAR
==================================================
∇ RXFCLEAR;I                                         
⍝ EXPUNGES THE VARIABLE RXRT DESCRIBING THE CURRENT
⍝ QUOTIENT ALGEBRA OF  R[X].                       
 I←⎕EX'RXRT'
∇
==================================================
FUNCTION: RXFDIFF
==================================================
∇ C←A RXFDIFF B                                 
⍝ COMPUTES THE DIFFERENCE OF TWO ARRAYS IN THE
⍝ CURRENT QUOTIENT ALGEBRA OF  R[X].          
 C←A RXFSUM-B
∇
==================================================
FUNCTION: RXFINIT
==================================================
∇ RXFINIT F;⎕IO;D;I                                  
⍝ INITIALIZES THE CURRENT QUOTIENT ALGEBRA OF R[X].
 ⎕IO←0                                             
 DERR 1×⍴⍴F                                        
 DERR 1≤D←¯1++/∨\⌽0≠F                              
 RXRT←((D-1),D)⍴-F←(÷F[D])×D↑F                     
 I←0                                               
LOOP:→((D-1)≤I←I+1)/0                              
 RXRT[I;]←(0,¯1↓RXRT[I-1;])-F×RXRT[I-1;D-1]        
 →LOOP
∇
==================================================
FUNCTION: RXFINV
==================================================
∇ r←RXFINV A;s;D;E                           
⍝ COMPUTES INVERSES IN THE CURRENT QUOTIENT
⍝ ALGEBRA OF  R[X].                        
 DERR(¯1↑⍴A)≤E←¯1↑⍴RXRT                    
 →(E=1)/SMALL                              
 D←A RXGCD(-RXRT[⎕IO;]),1                  
 DERR∧/(,D=1),1=¯1↑⍴D                      
 →0                                        
SMALL:r←÷A
∇
==================================================
FUNCTION: RXFPOWER
==================================================
∇ C←A RXFPOWER B;R;RHO;I;J;M;N;D                   
⍝ COMPUTES THE B-TH POWER OF  A  IN THE CURRENT  
⍝ QUOTIENT OF  R[X].                             
 B←((⍴B),1)⍴B                                    
 EXPANDV                                         
 DERR(M←¯1↑⍴A)≤N←¯1↑⍴RXRT                        
 R←×/RHO←¯1↓⍴A                                   
 A←(R,N)↑(R,M←¯1↑⍴A)⍴A                           
 C←(R,N)⍴N↑1                                     
 I←(B>0)/⍳⍴B←,B                                  
LOOP:C[J;]←((⍴J),N)↑C[J;]RXFPROD A[J←(2|B[I])/I;]
 →(0=⍴I←(B[I]≥2)/I)/END                          
 A[I;]←((⍴I),N)↑A[I;]RXFPROD A[I;]               
 B[I]←⌊B[I]÷2                                    
 →LOOP                                           
END:D←1⌈⌈/,+/∨\⌽0≠C                              
 C←(RHO,D)⍴(R,D)↑C
∇
==================================================
FUNCTION: RXFPROD
==================================================
∇ C←A RXFPROD B;D;E                                 
⍝ COMPUTES THE PRODUCT OF TWO ARRAYS OVER THE     
⍝ CURRENT QUOTIENT ALGEBRA OF R[X].               
 C←A RXPROD B                                     
 DERR(D←¯1↑⍴C)≤+/⍴RXRT                            
 →(D≤E←¯1↑⍴RXRT)/0                                
 C←(((¯1↓⍴C),E)↑C)+(((-⍴⍴C)↑E)↓C)+.×((D-E),E)↑RXRT
 D←1⌈+/∨\⌽∨⌿((×/¯1↓⍴C),E)⍴C≠0                     
 C←((¯1↓⍴C),D)↑C
∇
==================================================
FUNCTION: RXFSUM
==================================================
∇ C←A RXFSUM B;D;E                                  
⍝ COMPUTES THE SUM OF TWO ARRAYS OVER THE CURRENT 
⍝ QUOTIENT ALGEBRA OF R[X].                       
 D←¯1↑⍴C←A RXSUM B                                
 DERR D≤+/⍴RXRT                                   
 →(D≤E←¯1↑⍴RXRT)/0                                
 C←(((¯1↓⍴C),E)↑C)+(((-⍴⍴C)↑E)↓C)+.×((D-E),E)↑RXRT
 D←1⌈+/∨\⌽∨⌿((×/¯1↓⍴C),E)⍴C≠0                     
 C←((¯1↓⍴C),D)↑C
∇
==================================================
FUNCTION: RXGCD
==================================================
∇ C←A RXGCD B;⎕IO;M;U;V;R;RHO;I;Q;T;D;LA;LB;NOTEST;a  
⍝ COMPUTES MONIC GCD'S OF REAL POLYNOMIALS.  THE    
⍝ RESULT  C  IS  (r RXPROD A) RXSUM s RXPROD B.     
 ⎕IO←1                                              
 A←A×(|A)≥EPSILON×⌈/,|A                             
 B←B×(|B)≥EPSILON×⌈/,|B                             
 EXPANDV                                            
 M←1⌈+/∨\⌽∨⌿0≠((×/¯1↓⍴A),¯1↑⍴A)⍴A                   
 M←M⌈+/∨\⌽∨⌿0≠((×/¯1↓⍴B),¯1↑⍴B)⍴B                   
 R←×/RHO←¯1↓⍴A                                      
 NOTEST←1                                           
 A←(R,M)⍴(RHO,M)↑A RXPROD LA←(RHO,1)⍴÷RXLEAD A      
 B←(R,M)⍴(RHO,M)↑B RXPROD LB←(RHO,1)⍴÷RXLEAD B      
 U←((⍴A)↑(R,1)⍴LA),[1]((⍴A)⍴0),[0.5]A               
 V←((⍴B)⍴0),[1]((⍴B)↑(R,1)⍴LB),[0.5]B               
 I←⍳R                                               
LOOP:→(0=⍴I←(∨/V[3;I;]≠0)/I)/END                    
 Q←((⍴I),M)↑U[3;I;]RXQUOT V[3;I;]                   
 T←(3,(⍴I),M)↑U[;I;]RXDIFF V[;I;]RXPROD(3,⍴Q)⍴Q     
 T[3;;]←T[3;;]×(|T[3;;])≥⍉(⌽1↓⍴T)⍴EPSILON×⌈/|V[3;I;]
 T←(⍴T)↑T RXPROD(3,(⍴I),1)⍴÷RXLEAD T[3;;]           
 U[;I;]←V[;I;]                                      
 V[;I;]←T                                           
 →LOOP                                              
END:D←1⌈+/∨\⌽∨⌿0≠U[3;;]                             
 C←(RHO,D)⍴(R,D)↑U[3;;]                             
 D←1⌈+/∨\⌽∨⌿0≠U[1;;]                                
 r←(RHO,D)⍴(R,D)↑U[1;;]                             
 D←1⌈+/∨\⌽∨⌿0≠U[2;;]                                
 s←(RHO,D)⍴(R,D)↑U[2;;]
∇
==================================================
FUNCTION: RXGCD0
==================================================
∇ C←A RXGCD0 B;M;R;RHO;I;T;D;NOTEST                 
⍝ COMPUTES MONIC GCD'S OF REAL POLYNOMIALS WITHOUT
⍝ EXPRESSING THE RESULT AS A LINEAR COMBINATION   
⍝ OF THE ARGUMENTS.                               
 A←A×(|A)≥EPSILON×⌈/,|A                           
 B←B×(|B)≥EPSILON×⌈/,|B                           
 EXPANDV                                          
 M←1⌈+/∨\⌽0≠((×/¯1↓⍴A),¯1↑⍴A)⍴A                   
 M←M⌈+/∨\⌽0≠((×/¯1↓⍴B),¯1↑⍴B)⍴B                   
 I←⍳R←×/RHO←¯1↓⍴A                                 
 NOTEST←1                                         
 A←(R,M)⍴(RHO,M)↑A RXPROD(RHO,1)⍴÷RXLEAD A        
 B←(R,M)⍴(RHO,M)↑B RXPROD(RHO,1)⍴÷RXLEAD B        
LOOP:→(0=⍴I←(∨/B[I;]≠0)/I)/END                    
 T←((⍴I),M)↑B[I;]RXREM A[I;]                      
 T←T×(|T)≥EPSILON×(⌈/|B[I;])∘.×M⍴1                
 T←(⍴T)↑T RXPROD((⍴I),1)⍴÷RXLEAD T                
 A[I;]←B[I;]                                      
 B[I;]←T                                          
 →LOOP                                            
END:D←1⌈+/∨\⌽∨⌿0≠A                                
 C←(RHO,D)⍴(R,D)↑A
∇
==================================================
FUNCTION: RXINTERP
==================================================
∇ C←A RXINTERP B;⎕IO;D                              
⍝ INTERPOLATES REAL POLYNOMIALS.  THE VECTOR  A   
⍝ GIVES THE VALUES OF THE ARGUMENT AND THE VECTORS
⍝ ALONG THE LAST AXIS OF  B  GIVE THE VALUES THE  
⍝ POLYNOMIALS ARE TO HAVE.                        
 DERR∧/(1=⍴⍴A),(0<⍴A),(0<⍴⍴B),(⍴A)=¯1↑⍴B          
 ⎕IO←0                                            
 C←B+.×⌹⍉A∘.⋆⍳⍴A                                  
 C←C×(|C)≥EPSILON×⌈/,|C                           
 D←1⌈⌈/,+/∨\⌽0≠C                                  
 C←((¯1↓⍴C),D)↑C
∇
==================================================
FUNCTION: RXLEAD
==================================================
∇ C←RXLEAD A;⎕IO;D;RHO;I;R                          
⍝ COMPUTES THE ARRAY OF LEADING COEFFICIENTS OF AN
⍝ ARRAY OF REAL POLYNOMIALS.                      
 ⎕IO←0                                            
 →(0≠⍴⍴A)/NEXT                                    
 A←,A                                             
NEXT:RHO←¯1↓⍴A←A×(|A)≥EPSILON×⌈/,|A               
 D←,¯1++/∨\⌽0≠A                                   
 I←(D≥0)/⍳R←×/RHO                                 
 C←R⍴1                                            
 C[I]←(,A)[D[I]+(¯1↑⍴A)×I]                        
 C←RHO⍴C
∇
==================================================
FUNCTION: RXMATPROD
==================================================
∇ C←A RXMATPROD B;⎕IO;X;AX;BX;RR;D;NOTEST;RA;RB        
⍝ COMPUTES THE MATRIX PRODUCT OF TWO NONSCALAR ARRAYS
⍝ OF REAL POLYNOMIALS.                               
 ⎕IO←1                                               
 DERR∧/2≤(⍴⍴A),⍴⍴B                                   
 DERR(⍴A)[¯1+⍴⍴A]=1↑⍴B                               
 C←((RA←¯2↓⍴A),(RB←¯1↓1↓⍴B),1)⍴0                     
 X←1=⍳1↑⍴B                                           
 RR←((⍴RA)+⍳⍴RB),(⍳⍴RA),⍴⍴C                          
 NOTEST←1                                            
LOOP:AX←RR⍉(RB,RA,¯1↑⍴A)⍴X/[¯1+⍴⍴A]A                 
 BX←((¯1↓⍴C),¯1↑⍴B)⍴X⌿B                              
 C←C RXSUM AX RXPROD BX                              
 →(∼1↑X←¯1⌽X)/LOOP                                   
 D←1⌈⌈/,+/∨\⌽0≠C                                     
 C←((¯1↓⍴C),D)↑C
∇
==================================================
FUNCTION: RXPROD
==================================================
∇ C←A RXPROD B;⎕IO;D                                   
⍝ COMPUTES THE ENTRY-BY-ENTRY PRODUCT OF TWO ARRAYS  
⍝ OF REAL POLYNOMIALS.                               
 →NOTEST/BEGIN                                       
 EXPANDV                                             
BEGIN:⎕IO←0                                          
 C←(A∘.×(¯1↑⍴B)⍴1)×((⍳¯1+⍴⍴A),0 ¯1+⍴⍴A)⍉B∘.×(¯1↑⍴A)⍴1
 C←C,((⍴A),¯1+¯1↑⍴A)⍴0                               
 C←+/[¯2+⍴⍴C]((⍴A)⍴-⍳¯1↑⍴A)⌽C                        
 C←C×(|C)≥EPSILON×⌈/,|C                              
 D←1⌈⌈/,+/∨\⌽C≠0                                     
 C←((¯1↓⍴C),D)↑C
∇
==================================================
FUNCTION: RXPRODRED
==================================================
∇ C←RXPRODRED A;⎕IO;RHO;D;E;CC;L;M;NOTEST        
⍝ COMPUTES THE PRODUCT REDUCTION ALONG THE LAST
⍝ AXIS OF AN ARRAY OF REAL POLYNOMIALS.        
 →(1≥⍴⍴C←A)/0                                  
 ⎕IO←1                                         
 L←×/RHO←¯2↓⍴C                                 
 C←(L,¯2↑⍴C)⍴C                                 
 →(0=(⍴C)[2])/ZERO                             
 NOTEST←1                                      
LOOP:→(1=D←(⍴C)[2])/ONE                        
 CC←((L,E,¯1↑⍴C)↑C)RXPROD(L,(-E←⌊D÷2),¯1↑⍴C)↑C 
 →(D≠2×E)/ODD                                  
 C←CC                                          
 →LOOP                                         
ODD:M←(+/∨\⌽∨⌿0≠C[;E+1;])⌈¯1↑⍴CC               
 C←((L,M)↑C[;E+1;]),[2]((¯1↓⍴CC),M)↑CC         
 →LOOP                                         
ONE:C←(RHO,¯1↑⍴C)⍴C                            
 →0                                            
ZERO:C←(RHO,1)⍴1
∇
==================================================
FUNCTION: RXQUOT
==================================================
∇ C←A RXQUOT B;⎕IO;DB;N;K;L;R;I;F;D;E;RHO       
⍝ COMPUTES QUOTIENTS IN THE EUCLIDEAN DOMAIN  
⍝ OF REAL POLYNOMIALS.  THE REMAINDER IS SAVED
⍝ IN THE GLOBAL VARIABLE  a.                  
 ⎕IO←0                                        
 EXPANDV                                      
 DERR∧/,0≤DB←RXDEGREE B                       
 N←×/RHO←⍴DB                                  
 L←K⌈(+/¯1↑⍴A)+⌈/R←(¯1+K←+/¯1↑⍴B)-,DB         
 B←(-R)⌽(N,K)⍴B                               
 A←(-R)⌽(N,L)↑(N,¯1↑⍴A)⍴A                     
 C←(N,I←1++/L-K)⍴2-2                          
 E←÷B[;K-1]                                   
LOOP:→(0>I←I-1)/END                           
 C[;I]←F←A[;I+K-1]×E                          
 A[;I+⍳K]←A[;I+⍳K]-B×⍉(⌽⍴B)⍴F                 
 →LOOP                                        
END:C←C×(|C)≥EPSILON×⌈/,|C                    
 D←1⌈+/∨\⌽∨⌿C≠0                               
 C←(RHO,D)⍴(N,D)↑C                            
 A←A×(|A)≥EPSILON×⌈/(,|A),,|B                 
 D←1⌈+/∨\⌽∨⌿0≠A←R⌽A                           
 a←(RHO,D)⍴(N,D)↑A
∇
==================================================
FUNCTION: RXREDUCE
==================================================
∇ B←RXREDUCE A;⎕IO;I;J;K;L;M;N;Q;E;D;Y;Z;U;V;X;a         
⍝ REDUCES A MATRIX OF POLYNOMIALS IN  R[X]  USING      
⍝ ROW AND COLUMN OPERATIONS.  PRODUCES  MATRICES  r    
⍝ AND  s  SUCH THAT  B  IS THE MATRIX PRODUCT OF       
⍝ r,  A  AND  s.                                       
 DERR 3=⍴⍴A                                            
 B←A×(|A)≥EPSILON×⌈/,|A                                
 ⎕IO←0                                                 
 r←(K,K,1)⍴1,(K←1↑⍴B)⍴0                                
 s←(L,L,1)⍴1,(L←(⍴B)[1])⍴0                             
 I←¯1                                                  
LOOPI:→(∧/¯1=D←,RXDEGREE((I,I←I+1),0)↓B)/CLEANUP       
 V←I+((2↑⍴B)-I)⊤D⍳⌊/(D≥0)/D                            
 X←B[J←V[0];K←V[1];]                                   
COL:→(∧/¯1=D←RXDEGREE X RXREM B[;K;])/ROW              
 L←D⍳⌊/(D≥0)/D                                         
 Q←B[L;K;]RXQUOT X                                     
 E←Q RXPROD B[J;;]                                     
 B←((¯1↓⍴B),(¯1↑⍴B)⌈¯1↑⍴E)↑B                           
 B[L;;]←B[L;;]-(1↓⍴B)↑E                                
 E←Q RXPROD r[J;;]                                     
 r←((¯1↓⍴r),(¯1↑⍴r)⌈¯1↑⍴E)↑r                           
 r[L;;]←r[L;;]-(1↓⍴r)↑E                                
 B←B×(|B)≥EPSILON×⌈/,|B                                
 X←B[J←L;K;]                                           
 →COL                                                  
ROW:→(∧/¯1=D←RXDEGREE X RXREM B[J;;])/GENERAL          
 M←D⍳⌊/(D≥0)/D                                         
 Q←B[J;M;]RXQUOT X                                     
 E←Q RXPROD B[;M;]                                     
 B←((¯1↓⍴B),(¯1↑⍴B)⌈¯1↑⍴E)↑B                           
 B[;M;]←B[;M;]-(⍴B)[0 2]↑E                             
 E←Q RXPROD s[;M;]                                     
 S←((¯1↓⍴s),(¯1↑⍴s)⌈¯1↑⍴E)↑s                           
 s[;M;]←s[;M;]-(⍴s)[0 2]↑E                             
 B←B×(|B)≥EPSILON×⌈/,|B                                
 X←B[J;K←M;]                                           
 →COL                                                  
GENERAL:→(∧/¯1=D←,RXDEGREE X RXREM(I,I,0)↓B)/END       
 V←I+((2↑⍴B)-I)⊤D⍳⌊/(D≥0)/D                            
 Q←B[L←V[0];K;]RXQUOT X                                
 E←Q RXPROD B[J;;]                                     
 B←((¯1↓⍴B),(¯1↑⍴B)⌈¯1↑⍴E)↑B                           
 B[L;;]←B[L;;]-(1↓⍴B)↑E                                
 E←Q RXPROD r[J;;]                                     
 r←((¯1↓⍴r),(¯1↑⍴r)⌈¯1↑⍴E)↑r                           
 r[L;;]←r[L;;]-(1↓⍴r)↑E                                
 Q←B[L;M←V[1];]RXQUOT X                                
 E←Q RXPROD B[;K;]                                     
 B←((¯1↓⍴B),(¯1↑⍴B)⌈¯1↑⍴E)↑B                           
 B[;M;]←B[;M;]-(⍴B)[0 2]↑E                             
 E←Q RXPROD s[;K;]                                     
 s←((¯1↓⍴s),(¯1↑⍴s)⌈¯1↑⍴E)↑s                           
 s[;M;]←s[;M;]-(⍴s)[0 2]↑E                             
 B←B×(|B)≥EPSILON×⌈/,|B                                
 X←B[J←L;K←M;]                                         
 →COL                                                  
END:B[I,J;;]←B[J,I;;]                                  
 r[I,J;;]←r[J,I;;]                                     
 B[;I,K;]←B[;K,I;]                                     
 s[;I,K;]←s[;K,I;]                                     
 B[I;;]←B[I;;]×U←÷RXLEAD X                             
 r[I;;]←r[I;;]×U                                       
 Q←B[Y←(I+1)↓⍳1↑⍴B;I;]RXQUOT B[I;I;]                   
 E←(1 0 2⍉((⍴B)[1],⍴Q)⍴Q)RXPROD((1↑⍴Q),1↓⍴B)⍴B[I;;]    
 B←((¯1↓⍴B),(¯1↑⍴B)⌈¯1↑⍴E)↑B                           
 B[Y;;]←B[Y;;]-((⍴Y),1↓⍴B)↑E                           
 E←(1 0 2⍉((⍴r)[1],⍴Q)⍴Q)RXPROD((1↑⍴Q),1↓⍴r)⍴r[I;;]    
 r←((¯1↓⍴r),(¯1↑⍴r)⌈¯1↑⍴E)↑r                           
 r[Y;;]←r[Y;;]-((⍴Y),1↓⍴r)↑E                           
 Q←B[I;Z←(I+1)↓⍳(⍴B)[1];]RXQUOT B[I;I;]                
 B[I;Z;]←0                                             
 E←(1 0 2⍉((1↑⍴Q),(⍴s)[0 2])⍴s[;I;])RXPROD((1↑⍴s),⍴Q)⍴Q
 s←((¯1↓⍴s),(¯1↑⍴s)⌈¯1↑⍴E)↑s                           
 s[;Z;]←s[;Z;]-((1↑⍴s),(⍴Z),¯1↑⍴s)↑E                   
 B←B×(|B)≥EPSILON×⌈/,|B                                
 →LOOPI                                                
CLEANUP:D←1⌈+/∨\⌽∨⌿∨⌿0≠B                               
 B←((¯1↓⍴B),D)↑B                                       
 D←1⌈+/∨\⌽∨⌿∨⌿0≠r                                      
 r←((¯1↓⍴r),D)↑r                                       
 D←1⌈+/∨\⌽∨⌿∨⌿0≠s                                      
 s←((¯1↓⍴s),D)↑s
∇
==================================================
FUNCTION: RXREM
==================================================
∇ C←A RXREM B;a;Q                                  
⍝ COMPUTES THE REMAINDER OF  B  MODULO  A  IN THE
⍝ EUCLIDEAN DOMAIN OF REAL POLYNOMIALS.          
 Q←B RXQUOT A                                    
 C←a
∇
==================================================
FUNCTION: RXROWREDUCE
==================================================
∇ B←RXROWREDUCE A;IO;I;J;K;L;C;D;M;a               
⍝ ROW REDUCES A MATRIX OF POLYNOMIALS IN  R[X].  
⍝ PRODUCES AN INVERTIBLE MATRIX  r               
⍝ OF POLYNOMIALS SUCH THAT  B  IS  r RXMATPROD A.
⍝ THE VECTOR  v  LISTS THE COLUMNS OF THE CORNER 
⍝ ENTRIES OF  B.                                 
 DERR 3=⍴⍴A                                      
 B←A                                             
 IO←⎕IO                                          
 ⎕IO←1                                           
 v←⍳0                                            
 r←(K,K,1)⍴1,(K←1↑⍴B)⍴I←J←0                      
LOOP:→((J≥1↑⍴B)∨(⍴B)[2]<I←I+1)/END               
BACK:→(0=⍴D←(C≥0)/C←RXDEGREE(J,0)↓B[;I;])/LOOP   
 K←J+C⍳⌊/D                                       
 C←B[;I;]RXQUOT B[K;I;]                          
 C[K;]←0                                         
 D←2 1 3⍉((⍴B)[2],⍴C)⍴C                          
 B←B RXDIFF D RXPROD(⍴B)⍴B[K;;]                  
 D←2 1 3⍉((⍴r)[2],⍴C)⍴C                          
 r←r RXDIFF D RXPROD(⍴r)⍴r[K;;]                  
 →(1<+/∨/0≠(J,0)↓B[;I;])/BACK                    
 v←v,I                                           
 B[J,K;;]←B[K,J←J+1;;]                           
 r[J,K;;]←r[K,J;;]                               
 B[J;;]←B[J;;]×M←÷RXLEAD B[J;I;]                 
 r[J;;]←r[J;;]×M                                 
 →LOOP                                           
END:v←v-1-⎕IO←IO
∇
==================================================
FUNCTION: RXSUM
==================================================
∇ C←A RXSUM B;M;D                                      
⍝ COMPUTES THE SUM OF TWO ARRAYS OF REAL POLYNOMIALS.
 →NOTEST/BEGIN                                       
 EXPANDV                                             
BEGIN:M←(⍴A)⌈⍴B                                      
 C←(M↑A)+M↑B                                         
 C←C×(|C)≥EPSILON×⌈/,|C                              
 D←1⌈⌈/,+/∨\⌽0≠C                                     
 C←((¯1↓⍴C),D)↑C
∇
==================================================
FUNCTION: SCHV
==================================================
∇ A←N SCHV S;RS                                               
⍝ COMPUTES THE CHARACTERISTIC VECTORS OF AN ARRAY OF INTEGER
⍝ VECTORS LISTING SUBSETS OF  ⍳N.  ORIGIN DEPENDENT.        
 →NOTEST/BEGIN                                              
 DERR∧/(N>0),(N=⌊N),1=⍴N←,N                                 
 DERR∧/(,S=⌊S),(,S≥⎕IO),,S<⎕IO+N                            
 →(0<⍴⍴S)/BEGIN                                             
 S←,S                                                       
BEGIN:A←(N××/RS←¯1↓⍴S)⍴0                                    
 S←((×/RS),¯1↑⍴S)⍴S                                         
 A[⎕IO+N⊥((×/⍴S)⍴(⍳1↑⍴S)-⎕IO),[⎕IO-0.5],⍉S-⎕IO]←1           
 A←(RS,N)⍴A
∇
==================================================
FUNCTION: SEQREL
==================================================
∇ T←SEQREL E;X;NT                                
⍝ TESTS IF E IS THE CHARACTERISTIC MATRIX OF AN
⍝ EQUIVALENCE RELATION ON  ⍳1↑⍴E.  E  MUST BE A
⍝ SQUARE LOGICAL MATRIX.                       
 →NOTEST/BEGIN                                 
 DERR∧/(2=⍴⍴E),(=/⍴E),,Eϵ0 1                   
BEGIN:→(∼T←∧/(2⍴⎕IO)⍉E)/0                      
 NT←NOTEST                                     
 NOTEST←1                                      
 T←∧/,E=X∘.=X←SFEL E                           
 NOTEST←NT
∇
==================================================
FUNCTION: SETDIFF
==================================================
∇ C←A SETDIFF B    
⍝ EXERCISE 1.1.14
 C←(∼AϵB)/A
∇
==================================================
FUNCTION: SETEQ
==================================================
∇ T←A SETEQ B      
⍝ EXERCISE 1.1.14
 T←∧/(AϵB),BϵA
∇
==================================================
FUNCTION: SETINT
==================================================
∇ C←A SETINT B     
⍝ EXERCISE 1.1.14
 C←(AϵB)/A
∇
==================================================
FUNCTION: SETUN
==================================================
∇ C←A SETUN B      
⍝ EXERCISE 1.1.14
 C←SSORT A,B
∇
==================================================
FUNCTION: SFEL
==================================================
∇ R←SFEL A                                       
⍝ COMPUTES THE FIRST ELEMENTS IN THE SETS WHOSE
⍝ CHARACTERISTIC VECTORS ARE IN  A.            
⍝ THE SETS MUST BE NONEMPTY.                   
 →NOTEST/BEGIN                                 
 DERR(1≤⍴⍴A)∧∧/,∨/A                            
BEGIN:R←⎕IO++/∧\∼A
∇
==================================================
FUNCTION: SIEVE
==================================================
∇ P←SIEVE N;⎕IO;Q;N;M          
 ⎕IO←1                       
 P←⍳0                        
 Q←1↓⍳N                      
LOOP:→((0=⍴Q)∨N<M×M←1↑Q)/DONE
 P←P,M                       
 Q←(0≠M|Q)/Q                 
 →LOOP                       
DONE:P←P,Q
∇
==================================================
FUNCTION: SSORT
==================================================
∇ W←SSORT V                                         
⍝ SORTS A VECTOR INTO INCREASING ORDER AND REMOVES
⍝ DUPLICATES.                                     
 DERR 1=⍴⍴V                                       
 W←(1,(1↓W)>¯1↓W)/W←V[⍋V]
∇
==================================================
FUNCTION: SSUB
==================================================
∇ T←K SSUB N;X                                           
⍝ LISTS ALL K-ELEMENT SUBSETS OF  ⍳N. ORIGIN DEPENDENT.
 DERR∧/(K≥0),(K≤N),(1=⍴K),(1=⍴N),(N=⌊N←,N),K=⌊K←,K     
 →(∧/K≠0 1)/GENERAL                                    
 T←((K!N),K)⍴⍳N                                        
 →0                                                    
GENERAL:T←1+(K-1)SSUB N-1                              
 X←,T[;⎕IO]∘.>⍳N-1                                     
 T←(X/(⍴X)⍴⍳N-1),T[X/,⍉((N-1),1↑⍴T)⍴⍳1↑⍴T;]
∇
==================================================
FUNCTION: TRAV
==================================================
∇ B←TRAV A;R                       
⍝ TRANSPOSES AN ARRAY OF VECTORS.
 →(1≥⍴⍴A)/SMALL                  
 R←⍳⍴⍴A                          
 B←((⌽¯1↓R),¯1↑R)⍉A              
 →0                              
SMALL:B←A
∇
==================================================
FUNCTION: XXPOWER
==================================================
∇ G←F XXPOWER N    
⍝ EXERCISE 3.1.26
 G←⍳⍴F           
LOOP:→(N=0)/0    
 →(0=2|N)/EVEN   
 G←G[F]          
EVEN:F←F[F]      
 N←⌊N÷2          
 →LOOP
∇
==================================================
FUNCTION: ZACLEAR
==================================================
∇ ZACLEAR;I                                      
⍝ EXPUNGES THE ARRAY OF STRUCTURE CONSTANTS FOR
⍝ THE CURRENT Z-ALGEBRA.                       
 I←⎕EX'ZSC'
∇
==================================================
FUNCTION: ZADIFF
==================================================
∇ C←A ZADIFF B                                    
⍝ COMPUTES DIFFERENCES IN THE CURRENT Z-ALGEBRA.
 C←A ZASUM-B
∇
==================================================
FUNCTION: ZAINIT
==================================================
∇ ZAINIT A                                      
⍝ INITIALIZES THE ARRAY OF STRUCTURE CONSTANTS
⍝ FOR THE CURRENT Z-ALGEBRA.                  
 DERR∧/(3=⍴⍴A),((1↓⍴A)=¯1↓⍴A),,A=⌊A           
 ZSC←A
∇
==================================================
FUNCTION: ZANEG
==================================================
∇ C←ZANEG A                                     
⍝ COMPUTES NEGATIVES IN THE CURRENT Z-ALGEBRA.
 C←ZANRMLZ-A
∇
==================================================
FUNCTION: ZANRMLZ
==================================================
∇ C←ZANRMLZ A;⎕IO                                  
⍝ RETURNS THE STANDARD REPRESENTATION OF AN ARRAY
⍝ OVER THE THE CURRENT Z-ALGEBRA.  SCALARS AND   
⍝ VECTORS OF LENGTH 1 ARE PADDED WITH ZEROS.     
 ⎕IO←1                                           
 DERR∧/(,A=⌊A),(0=⍴⍴A)∨(1=¯1↑⍴A)∨(1↑⍴ZSC)=¯1↑⍴A  
 C←((⍴A),⍳0=⍴⍴A)⍴A                               
 →((1↑⍴ZSC)=¯1↑⍴C)/0                             
 C←((¯1↓⍴C),1↑⍴ZSC)↑C
∇
==================================================
FUNCTION: ZAPOWER
==================================================
∇ C←A ZAPOWER B;R;RHO;I;J;M                      
⍝ COMPUTES THE B-TH POWER OF  A  IN THE CURRENT
⍝ Z-ALGEBRA.                                   
 DERR∧/(,B=⌊B),,B≥0                            
 A←ZANRMLZ A                                   
 B←((⍴B),1)⍴B                                  
 EXPANDV                                       
 R←×/¯1↓RHO←⍴A                                 
 A←(R,M←¯1↑⍴A)⍴A                               
 C←(⍴A)⍴M↑1                                    
 I←(B>0)/⍳⍴B←,B                                
LOOP:C[J;]←C[J;]ZAPROD A[J←(2|B[I])/I;]        
 →(0=⍴I←(B[I]≥2)/I)/END                        
 A[I;]←A[I;]ZAPROD A[I;]                       
 B[I]←⌊B[I]÷2                                  
 →LOOP                                         
END:C←RHO⍴C
∇
==================================================
FUNCTION: ZAPROD
==================================================
∇ C←A ZAPROD B;⎕IO;R;RHO;M                     
⍝ COMPUTES PRODUCTS IN THE CURRENT Z-ALGEBRA.
 A←ZANRMLZ A                                 
 B←ZANRMLZ B                                 
 EXPANDV                                     
 R←×/¯1↓RHO←⍴A                               
 ⎕IO←0                                       
 M←¯1↑⍴ZSC                                   
 A←(R,M×M)⍴2 0 1⍉(M,R,M)⍴A                   
 B←(R,M×M)⍴1 0 2⍉(M,R,M)⍴B                   
 C←A×B                                       
 C←RHO⍴C+.×((M×M),M)⍴ZSC
∇
==================================================
FUNCTION: ZASUM
==================================================
∇ C←A ZASUM B                             
⍝ COMPUTE SUMS IN THE CURRENT Z-ALGEBRA.
 A←ZANRMLZ A                            
 B←ZANRMLZ B                            
 EXPANDV                                
 C←A+B
∇
==================================================
FUNCTION: ZCHREM
==================================================
∇ C←A ZCHREM B;⎕IO;r;s;RHO;D;L;M;N;B1;B2;A1;F;E;X       
⍝ SOLVES THE SIMULTANEOUS CONGRUENCE  C  CONGRUENT    
⍝ TO THE I-TH CROSS SECTION OF  A  ALONG THE LAST AXIS
⍝ MODULO B[I]. THE VARIABLE B MUST BE A VECTOR AND    
⍝ THE LCM OF THE COMPONENTS OF  B  IN COMPUTED AS  m. 
 ⎕IO←1                                                
 X←∧/(1=⍴⍴B),(1≤⍴⍴A),((¯1↑⍴A)=⍴B),(0<⍴B),,0≠B←|B      
 DERR∧/X,(,B=⌊B),,A=⌊A                                
 A←((N←×/RHO←¯1↓⍴A),¯1↑⍴A)⍴A                          
LOOP:→(1=M←⍴B)/END                                    
 L←B1×⌊B2÷D←(B1←E↑B)ZGCD B2←(-E←⌊M÷2)↑B               
 DERR∧/,0=((⍴F)⍴D)|F←((N,-E)↑A)-A1←(N,E)↑A            
 B←B[X←(E+1)×⍳M≠2×E],L                                
 A←(A[;X]),((⍴F)⍴L)|A1+(⌊F÷(⍴F)⍴D)×(⍴F)⍴r×B1          
 →LOOP                                                
END:m←B[1]                                            
 C←RHO⍴A
∇
==================================================
FUNCTION: ZDET
==================================================
∇ D←ZDET A;⎕IO;V;J;W;Q                           
⍝ COMPUTES THE DETERMINANT OF AN INTEGER MATRIX
⍝ USING INTEGER ROW OPERATIONS.                
 DERR∧/(,A=⌊A),(2=⍴⍴A),=/⍴A                    
 D←⎕IO←1                                       
 →(0=1↑⍴A)/0                                   
LOOP:→(1=1↑⍴A)/END                             
BACK:→(∧/0=V←|A[;1])/ZERO                      
 J←V⍳⌊/(V≠0)/V                                 
 →(J=1)/OK                                     
 A[1,J;]←A[J,1;]                               
 D←-D                                          
OK:→(∧/0=W←1↓A[;1])/ENDLP                      
 Q←0,(⌊W÷|A[1;1])××A[1;1]                      
 A←A-Q∘.×A[1;]                                 
 →BACK                                         
ENDLP:D←D×A[1;1]                               
 A←1 1↓A                                       
 →LOOP                                         
ZERO:→D←0                                      
END:D←D×A[1;1]
∇
==================================================
FUNCTION: ZFACTOR
==================================================
∇ P←ZFACTOR N;Q;R;⎕IO                                      
⍝ FACTORS A POSITIVE INTEGER INTO A PRODUCT OF PRIMES.   
⍝ THE RESULT IS CORRECT IF  N  IS LESS THAN 2.5E9.       
 DERR∧/(N=⌊N),(1≤N),1=⍴N←,N                              
 P←⍳⎕IO←0                                                
 Q←2 3 5,R←,(30×⍳77⌊⌈(N⋆0.5)÷30)∘.+7 11 13 17 19 23 29 31
LOOP:→(0=⍴Q←(0=Q|N)/Q)/NEXT                              
 P←P,1↑Q                                                 
 →LOOP,N←⌊N÷Q[0]                                         
NEXT:→(N=1)/0                                            
 →((¯1↑R)≥50000⌊N⋆0.5)/END                               
 →(R[0]≠7)/GEN                                           
 R←(∧⌿0≠7 11∘.|R)/R                                      
GEN:Q←R←R+2310                                           
 →LOOP                                                   
END:P←P,N
∇
==================================================
FUNCTION: ZGCD
==================================================
∇ C←A ZGCD B;⎕IO;RHO;M;U;V;I;Q;T                           
⍝ C  IS RETURNED AS THE ENTRY-BY-ENTRY GCD OF THE INTEGER
⍝ ARRAYS  A  AND  B.                                     
⍝ THE VARIABLES r AND s EXPRESS C AS(r×A)+s×B.           
 ⎕IO←1                                                   
 →NOTEST/BEGIN                                           
 DERR∧/(,A=⌊A),,B=⌊B                                     
⍝ TEST FOR CONFORMABILITY.                               
 EXPAND                                                  
⍝ REPLACE  A  AND  B  BY THEIR RAVELS AND                
⍝ APPLY THE EUCLIDEAN ALGORITHM.                         
BEGIN:M←×/RHO←⍴A                                         
 U←(3,M)⍴(×A),(M⍴0),|A←,A                                
 V←(⍴U)⍴(M⍴0),(×B),|B←,B                                 
 I←⍳M                                                    
LOOP:→(0=⍴I←(V[3;I]≠0)/I)/END                            
 T←U[;I]-V[;I]×(3,⍴I)⍴⌊U[3;I]÷V[3;I]                     
 U[;I]←V[;I]                                             
 V[;I]←T                                                 
 →LOOP                                                   
END:C←RHO⍴U[3;]                                          
 r←RHO⍴U[1;]                                             
 s←RHO⍴U[2;]
∇
==================================================
FUNCTION: ZGCD0
==================================================
∇ C←A ZGCD0 B;RHO;T;I                              
⍝ COMPUTES INTEGER GCD'S WITH A MINIMUM AMOUNT OF
⍝ CHECKING AND WITHOUT EXPRESSING THE RESULT AS A
⍝ LINEAR COMBINATION OF THE ARGUMENTS.           
 →NOTEST/BEGIN                                   
 DERR∧/(,A=⌊A),,B=⌊B                             
 EXPAND                                          
BEGIN:RHO←⍴A                                     
 I←⍳⍴A←|,A                                       
 B←|,B                                           
LOOP:→(0=⍴I←(B[I]≠0)/I)/END                      
 T←B[I]|A[I]                                     
 A[I]←B[I]                                       
 B[I]←T                                          
 →LOOP                                           
END:C←RHO⍴A
∇
==================================================
FUNCTION: ZLCM
==================================================
∇ C←A ZLCM B                              
⍝ COMPUTES THE ENTRY-BY-ENTRY LCM OF THE
⍝ INTEGER ARRAYS  A  AND  B.            
 C←(C≠0)×⌊(C←|A×B)÷A ZGCD0 B
∇
==================================================
FUNCTION: ZLSYS
==================================================
∇ C←A ZLSYS B;⎕IO;M;D;Q;r;s                           
⍝ SOLVES LINEAR SYSTEMS OVER THE INTEGERS.          
⍝ A  IS THE MATRIX OF COEFFICIENTS AND THE VECTORS  
⍝ OF CONSTANT TERMS ARE THE VECTORS ALONG THE FIRST 
⍝ AXIS OF  B.  THE ROWS OF THE GLOBAL ARRAY  w      
⍝ ARE A BASIS FOR THE SOLUTIONS OF THE CORRESPONDING
⍝ HOMOGENEOUS SYSTEM.                               
 ⎕IO←1                                              
 DERR∧/(2=⍴⍴A),(,A=⌊A),(,B=⌊B),(1≤⍴⍴B),(1↑⍴A)=1↑⍴B  
 D←(M←+/D≠0)↑D←1 1⍉A←ZREDUCE A                      
 DERR∧/,0=(M,(¯1+⍴⍴B)⍴0)↓B←r+.×B                    
 w←⍉(0,M)↓s                                         
 DERR∧/0=(Q←⍉(⌽⍴B)⍴D)|B←(M,1↓⍴B)↑B                  
 C←(((1↑⍴s),M)↑s)+.×⌊B÷Q
∇
==================================================
FUNCTION: ZMATINV
==================================================
∇ C←ZMATINV A;⎕IO;B;r;v                            
⍝ COMPUTES THE INVERSE OF THE SQUARE INTEGER     
⍝ MATRIX  A, WHICH MUST HAVE DETERMINANT 1 OR ¯1.
 DERR∧/(2=⍴⍴A),=/⍴A                              
 ⎕IO←1                                           
 B←ZROWREDUCE A                                  
 DERR∧/1=1 1⍉B                                   
 C←r
∇
==================================================
FUNCTION: ZNACLEAR
==================================================
∇ ZNACLEAR;I                                 
⍝ EXPUNGES THE ARRAY OF STRUCTURE CONSTANTS
⍝ FOR THE CURRENT ZN-ALGEBRA.              
 I←⎕EX'ZNSC'
∇
==================================================
FUNCTION: ZNADIFF
==================================================
∇ C←A ZNADIFF B                                    
⍝ COMPUTES DIFFERENCES IN THE CURRENT ZN-ALGEBRA.
 C←A ZNASUM-B
∇
==================================================
FUNCTION: ZNAINIT
==================================================
∇ ZNAINIT A                                     
⍝ INITIALIZES THE ARRAY OF STRUCTURE CONSTANTS
⍝ FOR THE CURRENT ZN-ALGEBRA.                 
 DERR∧/(3=⍴⍴A),((1↓⍴A)=¯1↓⍴A),,A=⌊A           
 ZNSC←n|A
∇
==================================================
FUNCTION: ZNANEG
==================================================
∇ C←ZNANEG A                                     
⍝ COMPUTES NEGATIVES IN THE CURRENT ZN-ALGEBRA.
 C←ZNANRMLZ n|-A
∇
==================================================
FUNCTION: ZNANRMLZ
==================================================
∇ C←ZNANRMLZ A;⎕IO                                 
⍝ RETURNS THE STANDARD REPRESENTATION OF AN ARRAY
⍝ OVER THE THE CURRENT ZN-ALGEBRA.  SCALARS AND  
⍝ VECTORS OF LENGTH 1 ARE PADDED WITH ZEROS.     
 ⎕IO←1                                           
 DERR∧/(,A=⌊A),(0=⍴⍴A)∨(1=¯1↑⍴A)∨(1↑⍴ZNSC)=¯1↑⍴A 
 C←((⍴A),⍳0=⍴⍴A)⍴n|A                             
 →((1↑⍴ZNSC)=¯1↑⍴C)/0                            
 C←((¯1↓⍴C),1↑⍴ZNSC)↑C
∇
==================================================
FUNCTION: ZNAPOWER
==================================================
∇ C←A ZNAPOWER B;R;RHO;I;J;M                     
⍝ COMPUTES THE B-TH POWER OF  A  IN THE CURRENT
⍝ ZN-ALGEBRA.  n  MUST NOT EXCEED 1E7.         
 DERR∧/(n≤1000000),(,B=⌊B),,B≥0                
 A←ZNANRMLZ A                                  
 B←((⍴B),1)⍴B                                  
 EXPANDV                                       
 R←×/¯1↓RHO←⍴A                                 
 A←(R,M←¯1↑⍴A)⍴A                               
 C←(⍴A)⍴M↑1                                    
 I←(B>0)/⍳⍴B←,B                                
LOOP:C[J;]←C[J;]ZNAPROD A[J←(2|B[I])/I;]       
 →(0=⍴I←(B[I]≥2)/I)/END                        
 A[I;]←A[I;]ZNAPROD A[I;]                      
 B[I]←⌊B[I]÷2                                  
 →LOOP                                         
END:C←RHO⍴C
∇
==================================================
FUNCTION: ZNAPROD
==================================================
∇ C←A ZNAPROD B;⎕IO;R;RHO;M                     
⍝ COMPUTES PRODUCTS IN THE CURRENT ZN-ALGEBRA.
⍝ n  MUST NOT EXCEED 1E7.                     
 DERR n≤10000000                              
 A←ZNANRMLZ A                                 
 B←ZNANRMLZ B                                 
 EXPANDV                                      
 R←×/¯1↓RHO←⍴A                                
 ⎕IO←0                                        
 M←¯1↑⍴ZNSC                                   
 A←(R,M×M)⍴2 0 1⍉(M,R,M)⍴A                    
 B←(R,M×M)⍴1 0 2⍉(M,R,M)⍴B                    
 C←n|A×B                                      
 C←RHO⍴n|C+.×((M×M),M)⍴ZNSC
∇
==================================================
FUNCTION: ZNASUM
==================================================
∇ C←A ZNASUM B                             
⍝ COMPUTE SUMS IN THE CURRENT ZN-ALGEBRA.
 A←ZNANRMLZ A                            
 B←ZNANRMLZ B                            
 EXPANDV                                 
 C←n|A+B
∇
==================================================
FUNCTION: ZNDET
==================================================
∇ D←ZNDET A;⎕IO;V;J;W;Q                          
⍝ COMPUTES THE DETERMINANT OF AN INTEGER MATRIX
⍝ USING INTEGER ROW OPERATIONS MODULO  n.      
 DERR∧/(n<10000000),(,A=⌊A),(2=⍴⍴A),=/⍴A←n|A   
 D←⎕IO←1                                       
 →(0=1↑⍴A)/0                                   
LOOP:→(1=1↑⍴A)/END                             
BACK:→(∧/0=V←A[;1])/ZERO                       
 J←V⍳⌊/(V≠0)/V                                 
 →(J=1)/OK                                     
 A[1,J;]←A[J,1;]                               
 D←n|-D                                        
OK:→(∧/0=W←1↓A[;1])/ENDLP                      
 Q←0,⌊W÷A[1;1]                                 
 A←n|A-Q∘.×A[1;]                               
 →BACK                                         
ENDLP:D←n|D×A[1;1]                             
 A←1 1↓A                                       
 →LOOP                                         
ZERO:→D←0                                      
END:D←n|D×A[1;1]
∇
==================================================
FUNCTION: ZNDIFF
==================================================
∇ C←A ZNDIFF B                                       
⍝ COMPUTES THE DIFFERENCE OF  A  AND  B  MODULO  n.
⍝ A  AND  B  MUST BE INTEGERS.                     
 →NOTEST/BEGIN                                     
 DERR∧/(,A=⌊A),,B=⌊B                               
BEGIN:C←n|A-B
∇
==================================================
FUNCTION: ZNINV
==================================================
∇ B←ZNINV A;r;s;D                                         
⍝ COMPUTES THE INVERSES OF THE ENTRIES OF  A  MODULO  n.
 DERR∧/,1=A ZGCD(⍴A)⍴n                                  
 B←n|r
∇
==================================================
FUNCTION: ZNLSYS
==================================================
∇ C←A ZNLSYS B;T;X;r;v                                
⍝ SOLVES LINEAR SYSTEMS OVER  ZN, WHERE  n  MUST BE 
⍝ PRIME.  PRODUCES AN ARRAY  C  SUCH THAT  A+.×C  IS
⍝ B  AND A MATRIX  w  WHOSE ROWS ARE A BASIS FOR THE
⍝ SOLUTION SPACE OF THE CORRESPONDING HOMOGENEOUS   
⍝ SYSTEM.                                           
 DERR∧/(1=⍴ZFACTOR n),(,A=⌊A),(,B=⌊B)               
 DERR∧/(2=⍴⍴A),(1≤⍴⍴B),(1↑⍴A)=1↑⍴B                  
 A←ZNROWREDUCE A                                    
 B←n|r+.×B                                          
 DERR∧/,0=((⍴v),(¯1+⍴⍴B)⍴0)↓B                       
 X←(∼T←(¯1↑⍴A)SCHV v)/⍳¯1↑⍴A                        
 w←((⍴X),⍴T)⍴0                                      
 w[;X]←X∘.=X                                        
 w[;v]←⍉n|-A[⍳⍴v;X]                                 
 C←T⍀((⍴v),1↓⍴B)↑B
∇
==================================================
FUNCTION: ZNMATINV
==================================================
∇ C←ZNMATINV A;⎕IO;B;r;v                      
⍝ COMPUTES THE INVERSE OF THE SQUARE INTEGER
⍝ MATRIX  A  MODULO  n.                     
 DERR∧/(2=⍴⍴A),=/⍴A                         
 ⎕IO←1                                      
 B←ZNROWREDUCE A                            
 DERR∧/1=1 1⍉B                              
 C←r
∇
==================================================
FUNCTION: ZNMATPROD
==================================================
∇ C←A ZNMATPROD B                                       
⍝ COMPUTES THE MATRIX PRODUCT OF THE ARRAYS  A  AND  B
⍝ MODULO  n, WHICH IS ASSUMED TO BE LESS THAN 1E7.    
 →NOTEST/BEGIN                                        
 DERR∧/(,A=A←n|A),(,B=⌊B←n|B),n<10000000              
BEGIN:C←n|A+.×B
∇
==================================================
FUNCTION: ZNNEG
==================================================
∇ B←ZNNEG A                                
⍝ COMPUTES THE NEGATIVE OF  A  MODULO  n.
⍝ A MUST BE AN INTEGER ARRAY.            
 →NOTEST/BEGIN                           
 DERR∧/,A=⌊A                             
BEGIN:B←n|-A
∇
==================================================
FUNCTION: ZNPOWER
==================================================
∇ C←A ZNPOWER B;RHO;I;J;NOTEST                        
⍝ COMPUTES  n|A⋆B  USING THE BINARY POWER ALGORITHM.
⍝ A  AND  B  MUST BE INTEGER ARRAYS AND  B≥0.       
 DERR∧/(,A=⌊A),(B=⌊B),,B≥0                          
 EXPAND                                             
 RHO←⍴A                                             
 C←(⍴A←,A)⍴1                                        
 I←(B>0)/⍳⍴B←,B                                     
 NOTEST←1                                           
LOOP:C[J]←C[J]ZNPROD A[J←(2|B[I])/I]                
 →(0=⍴I←(B[I]≥2)/I)/END                             
 A[I]←A[I]ZNPROD A[I]                               
 B[I]←⌊B[I]÷2                                       
 →LOOP                                              
END:C←RHO⍴C
∇
==================================================
FUNCTION: ZNPROD
==================================================
∇ C←A ZNPROD B;RHO;D;Q;⎕IO                                
⍝ COMPUTES  n|A×B  USING MULTIPLE PRECISION IF  n ≥ 1E7.
 →NOTEST/BEGIN                                          
 DERR∧/(,A=⌊A←n|A),,B=⌊B←n|B                            
BEGIN:→(n>10000000)/GEN                                 
 C←n|A×B                                                
 →0                                                     
GEN:EXPAND                                              
 RHO←⍴A                                                 
 ⎕IO←1                                                  
 D←(Q←3⍴M←1000000)⊤⌊((A←,A)×B←,B)÷n                     
 A←Q⊤A                                                  
 B←Q⊤B                                                  
 C←(5 3,1↓⍴A)↑((2 1 3⍉(3⍴1)∘.×A)×(3⍴1)∘.×B)-(Q⊤n)∘.×D   
 C←+/[2](0 ¯1 ¯2∘.×(1↓⍴A)⍴1)⌽[1]C                       
LOOP:C[1↓⍳5;]←¯499999+M|D←499999+1 0↓C                  
 C[⍳4;]←(¯1 0↓C)+⌊D÷M                                   
 →(∨/,0≠¯3 0↓C)/LOOP                                    
 C←n|RHO⍴M⊥2 0↓C
∇
==================================================
FUNCTION: ZNROWREDUCE
==================================================
∇ B←ZNROWREDUCE A;IO;I;J;K;L;M;X;U;GCD;s;Y;D;NOTEST;R        
⍝ ROW REDUCES  A  MODULO  n, WHICH MUST BE LESS            
⍝ THAN 1E7.  PRODUCES  r, AN INVERTIBLE MATRIX MODULO  n   
⍝ SUCH THAT  B  IS  r ZNMATPROD A, AND A VECTOR  v  LISTING
⍝ THE COLUMNS CONTAINING THE 'CORNER ENTRIES' OF  B.       
 DERR∧/(n<10000000),(,A=⌊A),2=⍴⍴A                          
 IO←⎕IO                                                    
 ⎕IO←NOTEST←1                                              
 L←¯1↑⍴B←n|A                                               
 R←(K,K)⍴1,(K←1↑⍴B)⍴0                                      
 v←⍳I←J←0                                                  
LOOP1:→((J≥K)∨L<I←I+1)/END                                 
LOOP2:→(∧/0=U←J↓B[;I])/LOOP1                               
 M←⌊/(U≠0)/U                                               
 X←J+U⍳M                                                   
 D←M ZGCD n                                                
 B[X;]←n|B[X;]×r                                           
 R[X;]←n|R[X;]×r                                           
 Y←(X≠⍳K)×B[;I]ZQUOT(1↑⍴B)⍴B[X;I]                          
 B←n|B-Y∘.×B[X;]                                           
 R←n|R-Y∘.×R[X;]                                           
 →(1=+/U≠0)/END1                                           
 →LOOP2                                                    
END1:v←v,I                                                 
 B[J,X;]←B[X,J←J+1;]                                       
 R[J,X;]←R[X,J;]                                           
 →LOOP1                                                    
END:v←v-1-⎕IO←IO                                           
 r←R
∇
==================================================
FUNCTION: ZNSUM
==================================================
∇ C←A ZNSUM B                                 
⍝ COMPUTES THE SUM OF  A  AND  B  MODULO  n.
⍝ A AND B MUST BE INTEGER ARRAYS.           
 →NOTEST/BEGIN                              
 DERR∧/(,A=⌊A),,B=⌊B                        
BEGIN:C←n|A+B
∇
==================================================
FUNCTION: ZNXDEGREE
==================================================
∇ B←ZNXDEGREE A                                    
⍝ COMPUTES THE DEGREES OF AN ARRAY OF POLYNOMIALS
⍝ OVER THE INTEGERS MODULO  n.                   
 B←ZXDEGREE n|A
∇
==================================================
FUNCTION: ZNXDET
==================================================
∇ D←ZNXDET A;⎕IO;DEG;J;V;W;Q;R;S;a;NOTEST                  
⍝ COMPUTES THE DETERMINANT OF A MATRIX OF INTEGER        
⍝ POLYNOMIALS MODULO  n, WHICH MUST BE A PRIME           
⍝ LESS THAN 1E7.                                         
 DERR∧/(,A=⌊A),(3=⍴⍴A),(=/2↑⍴A),(1=⍴ZFACTOR n),n<10000000
 A←n|A                                                   
 D←,⎕IO←NOTEST←1                                         
 →(0=1↑⍴A)/0                                             
LOOP:→(1=1↑⍴A)/END                                       
BACK:→(∧/¯1=DEG←¯1++/∨\⌽0≠A[;1;])/ZERO                   
 J←DEG⍳⌊/(DEG≠¯1)/DEG                                    
 →(J=1)/OK                                               
 A[1,J;;]←A[J,1;;]                                       
 D←n|-D                                                  
OK:→(∧/,0=W←(1 0)↓A[;1;])/ENDLP                          
 Q←(-1 0+⍴V)↑V←W ZNXQUOT(⍴W)⍴A[1;1;]                     
 R←TRAV((2↑⍴A),¯1↑⍴Q)⍴Q                                  
 S←(⍴A)⍴A[1;;]                                           
 A←A ZNXDIFF R ZNXPROD S                                 
 →BACK                                                   
ENDLP:D←D ZNXPROD A[1;1;]                                
 A←1 1 0↓A                                               
 →LOOP                                                   
ZERO:→D←,0                                               
END:D←D ZNXPROD A[1;1;]
∇
==================================================
FUNCTION: ZNXDIFF
==================================================
∇ C←A ZNXDIFF B                                         
⍝ COMPUTES THE DIFFERENCE OF TWO ARRAYS OF POLYNOMIALS
⍝ OVER THE INTEGERS MODULO  n.                        
 C←A ZNXSUM-B
∇
==================================================
FUNCTION: ZNXEVAL
==================================================
∇ Y←A ZNXEVAL B;I;NOTEST;⎕IO;RHO                      
⍝ EVALUATES THE POLYNOMIALS IN  A  AT  B  MODULO  n.
 DERR∧/(,A=⌊A),(,B=⌊B←((⍴B),1)⍴B),n<10000000        
 EXPANDV                                            
 A←((×/RHO←¯1↓⍴A),¯1↑⍴A)⍴n|A                        
 Y←(⍴B←,n|B)⍴0                                      
 ⎕IO←NOTEST←1                                       
 I←1+(⍴A)[2]                                        
LOOP:→(0≥I←I-1)/END                                 
 Y←n|A[;I]+B×Y                                      
 →LOOP                                              
END:Y←RHO⍴Y
∇
==================================================
FUNCTION: ZNXFACTOR
==================================================
∇ G←ZNXFACTOR F;⎕IO;M;R;D;H;U;I;V;E;J;W;a;CNT;UD;ZNXRT;F1  
⍝ COMPUTES THE MONIC IRREDUCIBLE FACTORS OF AN           
⍝ INTEGER POLYNOMIAL MODULO  n, WHICH MUST BE A          
⍝ PRIME LESS THAN 1E7.  THE ALGORITHM USED IS            
⍝ PROBABILISTIC AND SO HAS A SMALL CHANCE OF             
⍝ NOT FINDING ALL THE FACTORS.                           
 DERR∧/(n<10000000),(1=⍴ZFACTOR n),(1=⍴⍴F),,F=⌊F         
 DERR 0≤D←¯1++/∨\⌽F≠0                                    
 ⎕IO←0                                                   
 F←(D+1)↑n|F×ZNINV F[D]                                  
 G←(0,D+1)⍴M←0                                           
 R←0 1                                                   
LOOP:→((D←ZNXDEGREE F)<2×M←M+1)/END                      
 ZNXFINIT F                                              
 R←D↑(F ZNXREM R)ZNXFPOWER n                             
 →(1=⍴H←F ZNXGCD0 R-D↑0 1)/LOOP                          
 →(M=¯1+⍴H)/IRR                                          
 →(200>n⋆M)/SMALL                                        
 U←(1,⍴H)⍴H                                              
LOOPA:→(∧/M=UD←ZNXDEGREE U)/ENDA                         
 I←(M<UD)⍳1                                              
 ZNXFINIT F1←(1+E←UD[I])↑U[I;]                           
 CNT←0                                                   
LOOPA1:→(10<CNT←CNT+1)/ENDA1                             
 V←⍉(E⍴n)⊤?5⍴n⋆E                                         
 →(n=2)/EVEN                                             
 V←(5,E)↑V ZNXFPOWER(¯1+n⋆M)÷2                           
 V←(V∨.≠0)⌿V                                             
 V←(V∨.≠E↑1)⌿V                                           
 →(0=1↑⍴V←(V∨.≠E↑n-1)⌿V)/LOOPA1                          
 V←V[0;]                                                 
 →(1≠⍴W←(V+E↑1)ZNXGCD0 F1)/SPLIT                         
 W←V ZNXGCD0 F1                                          
 →SPLIT                                                  
EVEN:J←1                                                 
 W←V                                                     
LOOPA1A:→(M≤J←J+1)/ENDA1A                                
 W←n|W+V←V ZNXFPROD V                                    
 →LOOPA1A                                                
ENDA1A:W←(W∨.≠0)⌿W                                       
 →(0=1↑⍴W←(W∨.≠E↑1)⌿W)/LOOPA1                            
 W←F1 ZNXGCD0 W←W[0;]                                    
SPLIT:U←((I≠⍳1↑⍴U)⌿U),[0]((⍴H)↑W),[¯0.5](⍴H)↑F1 ZNXQUOT W
 →LOOPA                                                  
ENDA1:'BAD LUCK, YOU LOSE!'                              
 →                                                       
ENDA:G←G,[0]((1↑⍴U),¯1↑⍴G)↑U                             
 F←F ZNXQUOT H                                           
 →(1=⍴H←F ZNXGCD0 H)/LOOP                                
 U←((U ZNXREM H)∧.=0)⌿U                                  
 →ENDA                                                   
SMALL:U←(⍉(M⍴n)⊤⍳n⋆M),1                                  
 U←((U ZNXREM H)∧.=0)⌿U                                  
 →ENDA                                                   
IRR:G←G,[0](¯1↑⍴G)↑H                                     
 F←F ZNXQUOT H                                           
LOOPB:W←F ZNXQUOT H                                      
 →(a∨.≠0)/LOOP                                           
 G←G,[0](¯1↑⍴G)↑H                                        
 F←W                                                     
 →LOOPB                                                  
END:→(D=0)/ONE                                           
 G←G,[0](¯1↑⍴G)↑F                                        
ONE:D←ZNXDEGREE,G[¯1+1↑⍴G;]                              
 G←((1↑⍴G),D+1)↑G
∇
==================================================
FUNCTION: ZNXFCLEAR
==================================================
∇ ZNXFCLEAR;I                                         
⍝ EXPUNGES THE VARIABLE ZNXRT DESCRIBING THE CURRENT
⍝ QUOTIENT ALGEBRA OF ZN[X].                        
 I←⎕EX'ZNXRT'
∇
==================================================
FUNCTION: ZNXFDIFF
==================================================
∇ C←A ZNXFDIFF B                                
⍝ COMPUTES THE DIFFERENCE OF TWO ARRAYS IN THE
⍝ CURRENT QUOTIENT ALGEBRA OF  ZN[X].         
 C←A ZNXFSUM-B
∇
==================================================
FUNCTION: ZNXFINIT
==================================================
∇ ZNXFINIT F;D;⎕IO;I                                   
⍝ INITIALIZES THE CURRENT QUOTIENT ALGEBRA OF  ZN[X].
⍝ THE VALUE OF  n  MAY NOT EXCEED 1E7.               
 ⎕IO←0                                               
 DERR∧/(n<10000000),(1=⍴⍴F),,F=⌊F←n|F                
 DERR 1≤D←¯1++/∨\⌽0≠F                                
 ZNXRT←((D-1),D)⍴n|-F←n|(D↑F)×ZNINV F[D]             
 I←0                                                 
LOOP:→((D-1)≤I←I+1)/0                                
 ZNXRT[I;]←n|(0,¯1↓ZNXRT[I-1;])-F×ZNXRT[I-1;D-1]     
 →LOOP
∇
==================================================
FUNCTION: ZNXFINV
==================================================
∇ r←ZNXFINV A;s;D;E                          
⍝ COMPUTES INVERSES IN THE CURRENT QUOTIENT
⍝ ALGEBRA OF  ZN[X].  n  MUST BE PRIME.    
 DERR(¯1↑⍴A)≤E←¯1↑⍴ZNXRT                   
 →(E=1)/SMALL                              
 D←A ZNXGCD(-ZNXRT[⎕IO;]),1                
 DERR∧/(,D=1),1=¯1↑⍴D                      
 →0                                        
SMALL:r←ZNINV A
∇
==================================================
FUNCTION: ZNXFPOWER
==================================================
∇ C←A ZNXFPOWER B;D;E;RHO;R;I;J                        
⍝ COMPUTES POWERS IN THE CURRENT QUOTIENT ALGEBRA    
⍝ OF THE RING OF POLYNOMIALS OVER THE INTEGERS       
⍝ MODULO  n.  THE ENTRIES IN  B  MUST BE NONNEGATIVE 
⍝ INTEGERS.                                          
 DERR∧/(,B=⌊B),,B≥0                                  
 B←((⍴B),1)⍴B                                        
 EXPANDV                                             
 →((D←¯1↑⍴ZNXRT)≥E←¯1↑⍴A)/OK                         
 →(E>¯1+2×D)/DERR                                    
 A←n|(((¯1↓⍴A),D)↑A)+(((-⍴⍴A)↑D)↓A)+.×((E-D),D)↑ZNXRT
OK:A←((RHO←¯1↓⍴A),D)↑A                               
 A←((R←×/RHO),D)⍴A                                   
 C←(⍴A)⍴D↑1                                          
 I←(B>0)/⍳⍴B←,B                                      
LOOP:C[J;]←((⍴J),D)↑C[J;]ZNXFPROD A[J←(2|B[I])/I;]   
 →(0=⍴I←(B[I]≥2)/I)/END                              
 A[I;]←((⍴I),D)↑A[I;]ZNXFPROD A[I;]                  
 B[I]←⌊B[I]÷2                                        
 →LOOP                                               
END:D←1⌈+/∨\⌽∨⌿((×/¯1↓⍴C),D)⍴C≠0                     
 C←(RHO,D)⍴(R,D)↑C
∇
==================================================
FUNCTION: ZNXFPROD
==================================================
∇ C←A ZNXFPROD B;D;E                                   
⍝ COMPUTE THE PRODUCT OF TWO ARRAYS OVER THE         
⍝ CURRENT QUOTIENT ALGEBRA OF THE RING OF POLYNOMIALS
⍝ OVER THE INTEGERS MODULO  n.                       
 C←n|(n|A)ZXPROD n|B                                 
 DERR(D←¯1↑⍴C)≤+/⍴ZNXRT                              
 →(D≤E←¯1↑⍴ZNXRT)/0                                  
 C←n|(((¯1↓⍴C),E)↑C)+(((-⍴⍴C)↑E)↓C)+.×((D-E),E)↑ZNXRT
 D←1⌈+/∨\⌽∨⌿((×/¯1↓⍴C),E)⍴C≠0                        
 C←((¯1↓⍴C),D)↑C
∇
==================================================
FUNCTION: ZNXFSUM
==================================================
∇ C←A ZNXFSUM B;D;E                                    
⍝ COMPUTES THE SUM OF TWO ARRAYS OVER THE CURRENT    
⍝ QUOTIENT ALGEBRA OF THE RING OF POLYNOMIALS        
⍝ OVER THE INTEGERS MODULO  n.                       
 D←¯1↑⍴C←A ZNXSUM B                                  
 DERR D≤+/⍴ZNXRT                                     
 →(D≤E←¯1↑⍴ZNXRT)/0                                  
 C←n|(((¯1↓⍴C),E)↑C)+(((-⍴⍴C)↑E)↓C)+.×((D-E),E)↑ZNXRT
 D←1⌈+/∨\⌽∨⌿((×/¯1↓⍴C),E)⍴C≠0                        
 C←((¯1↓⍴C),D)↑C
∇
==================================================
FUNCTION: ZNXGCD
==================================================
∇ C←A ZNXGCD B;⎕IO;M;RHO;F;U;V;I;Q;T;D;LCI;a;R     
⍝ COMPUTES THE GCD OF TWO ARRAYS OF INTEGER      
⍝ POLYNOMIALS MODULO  n, WHICH MUST BE A PRIME   
⍝ LESS THAN 1E7.  THE RESULT  C  IS WRITTEN      
⍝ IN THE FORM  (r ZNXPROD A) ZNXSUM s ZNXPROD B. 
 DERR∧/(n<10000000),(1=⍴ZFACTOR n),(,A=⌊A),,B=⌊B 
 ⎕IO←1                                           
 EXPANDV                                         
 M←1⌈+/∨\⌽∨⌿0≠((×/¯1↓⍴A),¯1↑⍴A)⍴A←n|A            
 M←M⌈+/∨\⌽∨⌿0≠((×/¯1↓⍴B),¯1↑⍴B)⍴B←n|B            
 R←×/RHO←¯1↓⍴A                                   
 A←(R,M)⍴(RHO,M)↑A                               
 B←(R,M)⍴(RHO,M)↑B                               
 U←((⍴A)⍴M↑1),[1]((⍴A)⍴0),[0.5]A                 
 V←((⍴B)⍴0),[1]((⍴B)⍴M↑1),[0.5]B                 
 I←⍳R                                            
LOOP:→(0=⍴I←(∨/V[3;I;]≠0)/I)/END                 
 Q←((⍴I),M)↑U[3;I;]ZNXQUOT V[3;I;]               
 T←(3,(⍴I),M)↑U[;I;]ZNXDIFF V[;I;]ZNXPROD(3,⍴Q)⍴Q
 U[;I;]←V[;I;]                                   
 V[;I;]←T                                        
 →LOOP                                           
END:D←1⌈+/∨\⌽∨⌿0≠U[3;;]                          
 LCI←ZNINV(RHO,1)⍴ZNXLEAD C←(RHO,D)⍴(R,D)↑U[3;;] 
 C←C ZNXPROD LCI                                 
 D←1⌈+/∨\⌽∨⌿0≠U[1;;]                             
 r←LCI ZNXPROD(RHO,D)⍴(R,D)↑U[1;;]               
 D←1⌈+/∨\⌽∨⌿0≠U[2;;]                             
 s←LCI ZNXPROD(RHO,D)⍴(R,D)↑U[2;;]
∇
==================================================
FUNCTION: ZNXGCD0
==================================================
∇ C←A ZNXGCD0 B;M;R;RHO;I;T;D;LCI                 
⍝ COMPUTES GCD'S OF INTEGER POLYNOMIALS MODULO  
⍝ n  WITH A MINIMUM OF CHECKING AND WITHOUT     
⍝ EXPRESSING THE RESULT AS A LINEAR COMBINATION 
⍝ OF THE ARGUMENTS.                             
 DERR∧/(n<10000000),(1=⍴ZFACTOR n),(,A=⌊A),,B=⌊B
 EXPANDV                                        
 M←1⌈+/∨\⌽∨⌿0≠((×/¯1↓⍴A),¯1↑⍴A)⍴A←n|A           
 M←M⌈+/∨\⌽∨⌿0≠((×/¯1↓⍴B),¯1↑⍴B)⍴B←n|B           
 R←×/RHO←¯1↓⍴A                                  
 A←(R,M)⍴(RHO,M)↑A                              
 B←(R,M)⍴(RHO,M)↑B                              
 I←⍳R                                           
LOOP:→(0=⍴I←(∨/B[I;]≠0)/I)/END                  
 T←((⍴I),M)↑B[I;]ZNXREM A[I;]                   
 A[I;]←B[I;]                                    
 B[I;]←T                                        
 →LOOP                                          
END:D←1⌈+/∨\⌽∨⌿0≠A                              
 LCI←ZNINV(RHO,1)⍴ZNXLEAD C←(RHO,D)⍴(R,D)↑A     
 C←C ZNXPROD LCI
∇
==================================================
FUNCTION: ZNXIRRED
==================================================
∇ A←ZNXIRRED M;⎕IO;I;F;J;C                            
⍝ COMPUTES A MATRIX LISTING THE MONIC IRREDUCIBLE   
⍝ POLYNOMIALS OF DEGREE AT MOST  M OVER THE INTEGERS
⍝ MODULO  n, WHICH MUST BE A PRIME LESS THAN  1E7.  
 DERR∧/(n<10000000),(1=⍴ZFACTOR n),1≤M              
 ⎕IO←0                                              
 A←(0,M+1)⍴0                                        
 I←⍳1↑⍴C←ZNXMONIC M                                 
LOOP:A←A,[0]F←C[J←+/1↑I;]                           
 I←1↓I                                              
 →(M<2×ZXDEGREE F)/END                              
 I←(∨/0≠F ZNXREM C[I;])/I                           
 →LOOP                                              
END:A←A,[0]C[I;]
∇
==================================================
FUNCTION: ZNXLEAD
==================================================
∇ C←ZNXLEAD A;⎕IO;D;RHO;I;R                         
⍝ COMPUTES THE ARRAY OF LEADING COEFFICIENTS OF AN
⍝ ARRAY OF INTEGER POLYNOMIALS MODULO  n.         
 ⎕IO←0                                            
 →NOTEST/BEGIN                                    
 DERR∧/,A=⌊A                                      
 →(0≠⍴⍴A←n|A)/BEGIN                               
 A←,A                                             
BEGIN:RHO←¯1↓⍴A                                   
 D←,¯1++/∨\⌽0≠A                                   
 I←(D≥0)/⍳R←×/RHO                                 
 C←R⍴1                                            
 C[I]←(,A)[D[I]+(¯1↑⍴A)×I]                        
 C←RHO⍴C
∇
==================================================
FUNCTION: ZNXMATINV
==================================================
∇ C←ZNXMATINV A;⎕IO;B;r;v                                
⍝ COMPUTES THE INVERSE OF A SQUARE MATRIX  OVER  ZN[X].
 DERR∧/(3=⍴⍴A),=/¯1↓⍴A                                 
 ⎕IO←1                                                 
 B←ZNXROWREDUCE A                                      
 DERR∧/,(1 1 2⍉B)=(⍴B)[1 3]⍴(¯1↑⍴B)↑1                  
 C←r
∇
==================================================
FUNCTION: ZNXMATPROD
==================================================
∇ C←A ZNXMATPROD B;⎕IO;M;X;AX;BX;RR;RA;RB              
⍝ COMPUTES THE MATRIX PRODUCT OF TWO NONSCALAR ARRAYS
⍝ OF INTEGER POLYNOMIALS MODULO n.                   
 ⎕IO←1                                               
 DERR∧/(2≤(⍴⍴A),⍴⍴B),((⍴A)[¯1+⍴⍴A]=M←1↑⍴B)           
 C←((RA←¯2↓⍴A),(RB←¯1↓1↓⍴B),1)⍴0                     
 X←1=⍳M                                              
 RR←((⍴RA)+⍳⍴RB),(⍳⍴RA),⍴⍴C                          
LOOP:AX←RR⍉(RB,RA,¯1↑⍴A)⍴X/[¯1+⍴⍴A]A                 
 BX←((¯1↓⍴C),¯1↑⍴B)⍴X⌿B                              
 C←C ZNXSUM AX ZNXPROD BX                            
 →(∼1↑X←¯1⌽X)/LOOP
∇
==================================================
FUNCTION: ZNXMONIC
==================================================
∇ A←ZNXMONIC M;⎕IO;Q;I                                
⍝ COMPUTES A MATRIX LISTING THE MONIC POLYNOMIALS   
⍝ OF DEGREE AT MOST  M  OVER THE INTEGERS MODULO  n.
 ⎕IO←0                                              
 DERR∧/(1=⍴M),(,M=⌊M),,0<M←,M                       
 Q←1                                                
 A←⍳I←0                                             
LOOP:→(M<I←I+1)/ENCODE                              
 A←A,Q+⍳Q←Q×n                                       
 →LOOP                                              
ENCODE:A←⌽⍉((M+1)⍴n)⊤A
∇
==================================================
FUNCTION: ZNXPROD
==================================================
∇ C←A ZNXPROD B;D                                    
⍝ COMPUTES THE PRODUCT OF TWO ARRAYS OF POLYNOMIALS
⍝ OVER THE INTEGERS MODULO n.                      
 C←n|(n|A)ZXPROD n|B                               
 D←1⌈⌈/,+/∨\⌽0≠C                                   
 C←((¯1↓⍴C),D)↑C
∇
==================================================
FUNCTION: ZNXPRODRED
==================================================
∇ C←ZNXPRODRED A;⎕IO;RHO;D;E;CC;L;M                  
⍝ COMPUTES THE PRODUCT REDUCTION ALONG THE LAST    
⍝ AXIS OF AN ARRAY OF POLYNOMIALS OVER THE INTEGERS
⍝ MODULO  n, WHICH MUST NOT EXCEED 1E7.            
 →(1≥⍴⍴C←A)/0                                      
 ⎕IO←1                                             
 L←×/RHO←¯2↓⍴C                                     
 C←(L,¯2↑⍴C)⍴C                                     
 →(0=(⍴C)[2])/ZERO                                 
LOOP:→(1=D←(⍴C)[2])/ONE                            
 CC←((L,E,¯1↑⍴C)↑C)ZNXPROD(L,(-E←⌊D÷2),¯1↑⍴C)↑C    
 →(D≠2×E)/ODD                                      
 C←CC                                              
 →LOOP                                             
ODD:M←(+/∨\⌽∨⌿0≠C[;E+1;])⌈¯1↑⍴CC                   
 C←((L,M)↑C[;E+1;]),[2]((¯1↓⍴CC),M)↑CC             
 →LOOP                                             
ONE:C←(RHO,¯1↑⍴C)⍴C                                
 →0                                                
ZERO:C←(RHO,1)⍴1
∇
==================================================
FUNCTION: ZNXQUOT
==================================================
∇ C←A ZNXQUOT B;⎕IO;DB;N;K;L;R;I;F;D;E;RHO          
⍝ COMPUTES THE QUOTIENT OF  A  BY  B IN THE RING  
⍝ OF INTEGER POLYNOMIALS MODULO  n, WHICH MUST BE 
⍝ LESS THAN 1E7.  THE LEADING COEFFICIENTS IN  B  
⍝ MUST BE UNITS.  THE GLOBAL VARIABLE  a  CONTAINS
⍝ THE REMAINDERS.                                 
 ⎕IO←0                                            
 DERR∧/(,A=⌊A←n|A),(,B=⌊B←n|B),n<10000000         
 EXPANDV                                          
 DERR∧/,0≤DB←¯1++/∨\⌽0≠B                          
 N←×/RHO←⍴DB                                      
 L←K⌈(+/¯1↑⍴A)+⌈/R←(¯1+K←+/¯1↑⍴B)-,DB             
 B←(-R)⌽(N,K)⍴B                                   
 A←(-R)⌽(N,L)↑(N,¯1↑⍴A)⍴A                         
 C←(N,I←1++/L-K)⍴2-2                              
 E←ZNINV B[;K-1]                                  
LOOP:→(0>I←I-1)/END                               
 C[;I]←F←n|A[;I+K-1]×E                            
 A[;I+⍳K]←n|A[;I+⍳K]-B×⍉(⌽⍴B)⍴F                   
 →LOOP                                            
END:D←1⌈⌈/,+/∨\⌽0≠C                               
 C←(RHO,D)⍴(N,D)↑C                                
 D←1⌈⌈/,+/∨\⌽0≠A←R⌽A                              
 a←(RHO,D)⍴(N,D)↑A
∇
==================================================
FUNCTION: ZNXREDUCE
==================================================
∇ B←ZNXREDUCE A;⎕IO;I;J;K;L;M;N;Q;E;D;Y;Z;U;V;X;a         
⍝ REDUCES A MATRIX OF POLYNOMIALS IN  ZN[X]  USING      
⍝ ROW AND COLUMN OPERATIONS.  PRODUCES  MATRICES  r     
⍝ AND  s  SUCH THAT  B  IS THE MATRIX PRODUCT OF        
⍝ r,  A  AND  s.   n  MUST BE A PRIME.                  
 DERR∧/(1=⍴ZFACTOR n),(3=⍴⍴A),,A=⌊A                     
 B←n|A                                                  
 ⎕IO←0                                                  
 r←(K,K,1)⍴1,(K←1↑⍴B)⍴0                                 
 s←(L,L,1)⍴1,(L←(⍴B)[1])⍴0                              
 I←¯1                                                   
LOOPI:→(∧/¯1=D←,ZNXDEGREE((I,I←I+1),0)↓B)/CLEANUP       
 V←I+((2↑⍴B)-I)⊤D⍳⌊/(D≥0)/D                             
 X←B[J←V[0];K←V[1];]                                    
COL:→(∧/¯1=D←ZNXDEGREE X ZNXREM B[;K;])/ROW             
 L←D⍳⌊/(D≥0)/D                                          
 Q←B[L;K;]ZNXQUOT X                                     
 E←Q ZNXPROD B[J;;]                                     
 B←((¯1↓⍴B),(¯1↑⍴B)⌈¯1↑⍴E)↑B                            
 B[L;;]←n|B[L;;]-(1↓⍴B)↑E                               
 E←Q ZNXPROD r[J;;]                                     
 r←((¯1↓⍴r),(¯1↑⍴r)⌈¯1↑⍴E)↑r                            
 r[L;;]←n|r[L;;]-(1↓⍴r)↑E                               
 X←B[J←L;K;]                                            
 →COL                                                   
ROW:→(∧/¯1=D←ZNXDEGREE X ZNXREM B[J;;])/GENERAL         
 M←D⍳⌊/(D≥0)/D                                          
 Q←B[J;M;]ZNXQUOT X                                     
 E←Q ZNXPROD B[;M;]                                     
 B←((¯1↓⍴B),(¯1↑⍴B)⌈¯1↑⍴E)↑B                            
 B[;M;]←n|B[;M;]-(⍴B)[0 2]↑E                            
 E←Q ZNXPROD s[;M;]                                     
 S←((¯1↓⍴s),(¯1↑⍴s)⌈¯1↑⍴E)↑s                            
 s[;M;]←n|s[;M;]-(⍴s)[0 2]↑E                            
 X←B[J;K←M;]                                            
 →COL                                                   
GENERAL:→(∧/¯1=D←,ZNXDEGREE X ZNXREM(I,I,0)↓B)/END      
 V←I+((2↑⍴B)-I)⊤D⍳⌊/(D≥0)/D                             
 Q←B[L←V[0];K;]ZNXQUOT X                                
 E←Q ZNXPROD B[J;;]                                     
 B←((¯1↓⍴B),(¯1↑⍴B)⌈¯1↑⍴E)↑B                            
 B[L;;]←n|B[L;;]-(1↓⍴B)↑E                               
 E←Q ZNXPROD r[J;;]                                     
 r←((¯1↓⍴r),(¯1↑⍴r)⌈¯1↑⍴E)↑r                            
 r[L;;]←n|r[L;;]-(1↓⍴r)↑E                               
 Q←B[L;M←V[1];]ZNXQUOT X                                
 E←Q ZNXPROD B[;K;]                                     
 B←((¯1↓⍴B),(¯1↑⍴B)⌈¯1↑⍴E)↑B                            
 B[;M;]←n|B[;M;]-(⍴B)[0 2]↑E                            
 E←Q ZNXPROD s[;K;]                                     
 s←((¯1↓⍴s),(¯1↑⍴s)⌈¯1↑⍴E)↑s                            
 s[;M;]←n|s[;M;]-(⍴s)[0 2]↑E                            
 X←B[J←L;K←M;]                                          
 →COL                                                   
END:B[I,J;;]←B[J,I;;]                                   
 r[I,J;;]←r[J,I;;]                                      
 B[;I,K;]←B[;K,I;]                                      
 s[;I,K;]←s[;K,I;]                                      
 B[I;;]←n|B[I;;]×U←ZNINV ZNXLEAD X                      
 r[I;;]←n|r[I;;]×U                                      
 Q←B[Y←(I+1)↓⍳1↑⍴B;I;]ZNXQUOT B[I;I;]                   
 E←(1 0 2⍉((⍴B)[1],⍴Q)⍴Q)ZNXPROD((1↑⍴Q),1↓⍴B)⍴B[I;;]    
 B←((¯1↓⍴B),(¯1↑⍴B)⌈¯1↑⍴E)↑B                            
 B[Y;;]←n|B[Y;;]-((⍴Y),1↓⍴B)↑E                          
 E←(1 0 2⍉((⍴r)[1],⍴Q)⍴Q)ZNXPROD((1↑⍴Q),1↓⍴r)⍴r[I;;]    
 r←((¯1↓⍴r),(¯1↑⍴r)⌈¯1↑⍴E)↑r                            
 r[Y;;]←n|r[Y;;]-((⍴Y),1↓⍴r)↑E                          
 Q←B[I;Z←(I+1)↓⍳(⍴B)[1];]ZNXQUOT B[I;I;]                
 B[I;Z;]←0                                              
 E←(1 0 2⍉((1↑⍴Q),(⍴s)[0 2])⍴s[;I;])ZNXPROD((1↑⍴s),⍴Q)⍴Q
 s←((¯1↓⍴s),(¯1↑⍴s)⌈¯1↑⍴E)↑s                            
 s[;Z;]←n|s[;Z;]-((1↑⍴s),(⍴Z),¯1↑⍴s)↑E                  
 →LOOPI                                                 
CLEANUP:D←1⌈+/∨\⌽∨⌿∨⌿0≠B                                
 B←((¯1↓⍴B),D)↑B                                        
 D←1⌈+/∨\⌽∨⌿∨⌿0≠r                                       
 r←((¯1↓⍴r),D)↑r                                        
 D←1⌈+/∨\⌽∨⌿∨⌿0≠s                                       
 s←((¯1↓⍴s),D)↑s
∇
==================================================
FUNCTION: ZNXREM
==================================================
∇ C←A ZNXREM B;a;Q                                 
⍝ COMPUTES THE REMAINDER OF  B  MODULO  A  IN THE
⍝ EUCLIDEAN DOMAIN OF POLYNOMIALS MOD  n, WHICH  
⍝ MUST BE A PRIME SMALLER THAN 1E7.              
 Q←B ZNXQUOT A                                   
 C←a
∇
==================================================
FUNCTION: ZNXROWREDUCE
==================================================
∇ B←ZNXROWREDUCE A;IO;I;J;K;L;C;D;M;a                   
⍝ ROW REDUCES A MATRIX OF POLYNOMIALS IN  ZN[X].      
⍝ n MUST BE A PRIME.  PRODUCES AN INVERTIBLE MATRIX  r
⍝ OF POLYNOMIALS SUCH THAT  B  IS  r ZNXMATPROD A.    
⍝ THE VECTOR  v  LISTS THE CORNER ENTRIES OF  B.      
 DERR∧/(1=⍴ZFACTOR n),(3=⍴⍴A),,A=⌊A                   
 B←n|A                                                
 IO←⎕IO                                               
 ⎕IO←1                                                
 v←⍳0                                                 
 r←(K,K,1)⍴1,(K←1↑⍴B)⍴I←J←0                           
LOOP:→((J≥1↑⍴B)∨(⍴B)[2]<I←I+1)/END                    
BACK:→(0=⍴D←(C≥0)/C←ZNXDEGREE(J,0)↓B[;I;])/LOOP       
 K←J+C⍳⌊/D                                            
 C←B[;I;]ZNXQUOT B[K;I;]                              
 C[K;]←0                                              
 D←2 1 3⍉((⍴B)[2],⍴C)⍴C                               
 B←B ZNXDIFF D ZNXPROD(⍴B)⍴B[K;;]                     
 D←2 1 3⍉((⍴r)[2],⍴C)⍴C                               
 r←r ZNXDIFF D ZNXPROD(⍴r)⍴r[K;;]                     
 →(1<+/∨/0≠(J,0)↓B[;I;])/BACK                         
 v←v,I                                                
 B[J,K;;]←B[K,J←J+1;;]                                
 r[J,K;;]←r[K,J;;]                                    
 B[J;;]←n|B[J;;]×M←ZNINV ZNXLEAD B[J;I;]              
 r[J;;]←n|r[J;;]×M                                    
 →LOOP                                                
END:v←v-1-⎕IO←IO
∇
==================================================
FUNCTION: ZNXSUM
==================================================
∇ C←A ZNXSUM B;D                                    
⍝ COMPUTES THE SUM OF TWO ARRAYS OF POLYNOMIALS OF
⍝ INTEGERS MODULO  n.                             
 C←n|(n|A)ZXSUM n|B                               
 D←1⌈⌈/,+/∨\⌽0≠C                                  
 C←((¯1↓⍴C),D)↑C
∇
==================================================
FUNCTION: ZPRIMES
==================================================
∇ P←ZPRIMES N;⎕IO;Q;R                     
⍝ LISTS THE PRIMES UP TO N.             
 ⎕IO←0                                  
 DERR 1=⍴N←,N                           
 P←(N≥P)/P←2 3 5 7 11 13 17 19          
 →(N≤22)/0                              
 Q←,(30×⍳⌈N÷30)∘.+7 11 13 17 19 23 29 31
 Q←(∧⌿0≠7 11 13 17 19∘.|Q)/Q            
LOOP:→((0=⍴Q)∨N<(1↑Q)⋆2)/END            
 P←P,R←(5⌊⍴Q)↑Q                         
 Q←(∧⌿0≠R∘.|Q)/Q                        
 →LOOP                                  
END:P←(N≥P)/P←P,Q
∇
==================================================
FUNCTION: ZQUOT
==================================================
∇ C←A ZQUOT B                                           
⍝ COMPUTES THE INTEGER QUOTIENT OF TWO INTEGER ARRAYS.
 →NOTEST/BEGIN                                        
 DERR∧/(,A=⌊A),,B=⌊B                                  
BEGIN:C←(⌊A÷|B)××B
∇
==================================================
FUNCTION: ZREDUCE
==================================================
∇ B←ZREDUCE A;⎕IO;I;J;K;L;M;Q;D;Y;Z;X;V              
⍝ REDUCES AN INTEGER MATRIX.  PRODUCES INVERTIBLE  
⍝ INTEGER MATRICES  r  AND  s  SUCH THAT  B  IS    
⍝ THE MATRIX PRODUCT OF  r,  A  AND  s.            
 ⎕IO←0                                             
 DERR∧/(2=⍴⍴A),,B=⌊B←A                             
 r←(K,K)⍴1,(K←1↑⍴B)⍴0                              
 s←(L,L)⍴1,(L←1↓⍴B)⍴0                              
 I←¯1                                              
LOOPI:→(∧/0=D←|,(I,I←I+1)↓B)/0                     
 V←I+((⍴B)-I)⊤D⍳⌊/(D≠0)/D                          
 X←B[J←V[0];K←V[1]]                                
COL:→(∧/0=D←|X|B[;K])/ROW                          
 L←D⍳⌊/(D≠0)/D                                     
 B[L;]←B[L;]-(Q←⌊(B[L;K]-X|B[L;K])÷X)×B[J;]        
 r[L;]←r[L;]-Q×r[J;]                               
 X←B[J←L;K]                                        
 →COL                                              
ROW:→(∧/0=D←|X|B[J;])/GENERAL                      
 M←D⍳⌊/(D≠0)/D                                     
 B[;M]←B[;M]-(Q←⌊(B[J;M]-X|B[J;M])÷X)×B[;K]        
 s[;M]←s[;M]-Q×s[;K]                               
 X←B[J;K←M]                                        
 →COL                                              
GENERAL:→(∧/0=D←|X|,(I,I)↓B)/END                   
 V←I+((⍴B)-I)⊤D⍳⌊/(D≠0)/D                          
 B[L;]←B[L;]-(Q←¯1+⌊B[L←V[0];K]÷X)×B[J;]           
 r[L;]←r[L;]-Q×r[J;]                               
 B[;M]←B[;M]-(Q←⌊(B[L;M]-X|B[L;M←V[1]])÷X)×B[;K]   
 s[;M]←s[;M]-Q×s[;K]                               
 X←B[J←L;K←M]                                      
 →COL                                              
END:B[I,J;]←B[J,I;]                                
 r[I,J;]←r[J,I;]                                   
 B[;I,K]←B[;K,I]                                   
 s[;I,K]←s[;K,I]                                   
 B[I;]←B[I;]××X                                    
 r[I;]←r[I;]××X                                    
 B[Y;]←B[Y;]-(Q←⌊B[Y←(I+1)↓⍳1↑⍴B;I]÷B[I;I])∘.×B[I;]
 r[Y;]←r[Y;]-Q∘.×r[I;]                             
 B[;Z]←B[;Z]-B[;I]∘.×Q←⌊B[I;Z←(I+1)↓⍳1↓⍴B]÷B[I;I]  
 s[;Z]←s[;Z]-s[;I]∘.×Q                             
 →LOOPI
∇
==================================================
FUNCTION: ZREM
==================================================
∇ C←A ZREM B                                         
⍝ COMPUTES THE REMAINDER WHEN  B  IS DIVIDED BY  A.
⍝BOTH ARRAYS MUST BE INTEGER.                      
 →NOTEST/BEGIN                                     
 DERR∧/(,A=⌊A),,B=⌊B                               
BEGIN:C←(|A)|B
∇
==================================================
FUNCTION: ZROWREDUCE
==================================================
∇ B←ZROWREDUCE A;IO;I;J;K;L;D;E;F;X;Y;N;M                  
⍝ ROW REDUCES THE INTEGER MATRIX  A.  PRODUCES  r, AN    
⍝ INVERTIBLE INTEGER MATRIX SUCH THAT  B  IS  r+.×A.     
⍝ ALSO PRODUCES A VECTOR v LISTING THE COLUMNS CONTAINING
⍝ THE CORNER ENTRIES OF B.                               
 DERR∧/(2=⍴⍴A),,A=⌊A                                     
 IO←⎕IO                                                  
 ⎕IO←1                                                   
 L←¯1↑⍴B←A                                               
 r←(K,K)⍴1,(K←1↑⍴B)⍴0                                    
 v←⍳I←J←0                                                
LOOP:→((J≥K)∨L<I←I+1)/END                                
BACK:→(0=⍴D←(E≠0)/E←|J↓B[;I])/LOOP                       
 X←J+E⍳N←⌊/D                                             
 F←((X≠Y←J↓⍳K)×J↓B[;I])ZQUOT B[X;I]                      
 B[Y;]←((J,0)↓B)-F∘.×B[X;]                               
 r[Y;]←((J,0)↓r)-F∘.×r[X;]                               
 →(1<+/0≠J↓B[;I])/BACK                                   
 v←v,I                                                   
 B[J,X;]←B[X,J←J+1;]                                     
 r[J,X;]←r[X,J;]                                         
 B[J;]←B[J;]×M←×B[J;I]                                   
 r[J;]←r[J;]×M                                           
 F←B[Y←⍳J-1;I]ZQUOT B[J;I]                               
 B[Y;]←B[Y;]-F∘.×B[J;]                                   
 r[Y;]←r[Y;]-F∘.×r[J;]                                   
 →LOOP                                                   
END:v←v-1-⎕IO←IO
∇
==================================================
FUNCTION: ZXDEGREE
==================================================
∇ B←ZXDEGREE A                                          
⍝ COMPUTES THE ARRAY OF DEGREES OF AN ARRAY OF INTEGER
⍝ POLYNOMIALS.                                        
 →NOTEST/BEGIN                                        
 DERR∧/,A=⌊A                                          
 →(0<⍴⍴A)/BEGIN                                       
 A←,A                                                 
BEGIN:B←¯1++/∨\⌽A≠0
∇
==================================================
FUNCTION: ZXDIFF
==================================================
∇ C←A ZXDIFF B                                      
⍝ COMPUTES THE DIFFERENCE OF TWO ARRAYS OF INTEGER
⍝ POLYNOMIALS.                                    
 C←A ZXSUM-B
∇
==================================================
FUNCTION: ZXEVAL
==================================================
∇ Y←A ZXEVAL B;⎕IO                                 
⍝ EVALUATES THE INTEGER POLYNOMIALS IN  A  AT  B.
 ⎕IO←0                                           
 DERR∧/(,A=⌊A),,B=⌊B                             
 B←((⍴B),1)⍴B                                    
 EXPANDV                                         
 B←(¯1↓⍴B)⍴B                                     
 Y←+/A×B∘.⋆⍳¯1↑⍴A
∇
==================================================
FUNCTION: ZXFCLEAR
==================================================
∇ ZXFCLEAR;I                                         
⍝ EXPUNGES THE VARIABLE ZXRT DESCRIBING THE CURRENT
⍝ QUOTIENT ALGEBRA OF  Z[X].                       
 I←⎕EX'ZXRT'
∇
==================================================
FUNCTION: ZXFDIFF
==================================================
∇ C←A ZXFDIFF B                                 
⍝ COMPUTES THE DIFFERENCE OF TWO ARRAYS IN THE
⍝ CURRENT QUOTIENT ALGEBRA OF  Z[X].          
 C←A ZXFSUM-B
∇
==================================================
FUNCTION: ZXFINIT
==================================================
∇ ZXFINIT F;⎕IO;D;I                                  
⍝ INITIALIZES THE CURRENT QUOTIENT ALGEBRA OF Z[X].
 ⎕IO←0                                             
 DERR∧/(1=⍴⍴F),,F=⌊F                               
 DERR 1≤D←¯1++/∨\⌽0≠F                              
 DERR 1=|F[D]                                      
 ZXRT←((D-1),D)⍴-F←F[D]×D↑F                        
 I←0                                               
LOOP:→((D-1)≤I←I+1)/0                              
 ZXRT[I;]←(0,¯1↓ZXRT[I-1;])-F×ZXRT[I-1;D-1]        
 →LOOP
∇
==================================================
FUNCTION: ZXFPOWER
==================================================
∇ C←A ZXFPOWER B;R;RHO;I;J;M;N;D                   
⍝ COMPUTES THE B-TH POWER OF  A  IN THE CURRENT  
⍝ QUOTIENT OF  R[X].                             
 B←((⍴B),1)⍴B                                    
 EXPANDV                                         
 N←¯1↑⍴ZXRT                                      
 R←×/RHO←¯1↓⍴A                                   
 A←(R,M←¯1↑⍴A)⍴A                                 
 C←(R,N)⍴N↑1                                     
 I←(B>0)/⍳⍴B←,B                                  
LOOP:C[J;]←((⍴J),N)↑C[J;]ZXFPROD A[J←(2|B[I])/I;]
 →(0=⍴I←(B[I]≥2)/I)/END                          
 A[I;]←A[I;]ZXFPROD A[I;]                        
 B[I]←⌊B[I]÷2                                    
 →LOOP                                           
END:D←1⌈⌈/,+/∨\⌽0≠C                              
 C←(RHO,D)⍴(R,D)↑C
∇
==================================================
FUNCTION: ZXFPROD
==================================================
∇ C←A ZXFPROD B;D;E                                 
⍝ COMPUTE THE PRODUCT OF TWO ARRAYS OVER THE      
⍝ CURRENT QUOTIENT ALGEBRA OF Z[X].               
 C←A ZXPROD B                                     
 DERR(D←¯1↑⍴C)≤+/⍴ZXRT                            
 →(D≤E←¯1↑⍴ZXRT)/0                                
 C←(((¯1↓⍴C),E)↑C)+(((-⍴⍴C)↑E)↓C)+.×((D-E),E)↑ZXRT
 D←1⌈+/∨\⌽∨⌿((×/¯1↓⍴C),E)⍴C≠0                     
 C←((¯1↓⍴C),D)↑C
∇
==================================================
FUNCTION: ZXFSUM
==================================================
∇ C←A ZXFSUM B;D;E                                  
⍝ COMPUTES THE SUM OF TWO ARRAYS OVER THE CURRENT 
⍝ QUOTIENT ALGEBRA OF Z[X].                       
 D←¯1↑⍴C←A ZXSUM B                                
 DERR D≤+/⍴ZXRT                                   
 →(D≤E←¯1↑⍴ZXRT)/0                                
 C←(((¯1↓⍴C),E)↑C)+(((-⍴⍴C)↑E)↓C)+.×((D-E),E)↑ZXRT
 D←1⌈+/∨\⌽∨⌿((×/¯1↓⍴C),E)⍴C≠0                     
 C←((¯1↓⍴C),D)↑C
∇
==================================================
FUNCTION: ZXINTERP
==================================================
∇ C←A ZXINTERP B;⎕IO;L;RHO;RC;G;I;M;N;NOTEST;D             
⍝ INTERPOLATES INTEGER POLYNOMIALS.  THE VECTOR  A       
⍝ GIVES THE INTEGER VALUES OF THE ARGUMENT AND THE       
⍝ VECTORS ALONG THE LAST AXIS OF  B  GIVE THE INTEGER    
⍝ VALUES WHICH THE POLYNOMIALS ARE TO HAVE.              
 ⎕IO←1                                                   
 DERR∧/(1=⍴⍴A),(0<⍴A),(A=⌊A),(,B=⌊B),(0<⍴⍴B),(1↑⍴A)=¯1↑⍴B
 RC←×/RHO←¯1↓⍴B                                          
 B←(RC,L←⍴A)⍴B                                           
 C←(RC,1)⍴B[;1]                                          
 G←(-A[1]),1                                             
 NOTEST←I←1                                              
LOOP:→(L<I←I+1)/END                                      
 M←(RC,1)⍴B[;I]-C ZXEVAL RC⍴A[I]                         
 N←G ZXEVAL A[I]                                         
 DERR∧/,0=N|M                                            
 C←C ZXSUM((RC,⍴G)⍴G)ZXPROD⌊M÷N                          
 G←G ZXPROD(-A[I]),1                                     
 →LOOP                                                   
END:C←(RHO,¯1↑⍴C)⍴C                                      
 D←1⌈⌈/,+/∨\⌽C≠0                                         
 C←(RHO,D)↑C
∇
==================================================
FUNCTION: ZXLEAD
==================================================
∇ C←ZXLEAD A;EPSILON                                
⍝ COMPUTES THE LEADING COEFFICIENTS OF AN ARRAY OF
⍝ INTEGER POLYNOMIALS.                            
 EPSILON←0                                        
 C←RXLEAD A
∇
==================================================
FUNCTION: ZXMATPROD
==================================================
∇ C←A ZXMATPROD B;⎕IO;X;AX;BX;RR;RA;RB;NOTEST          
⍝ COMPUTES THE MATRIX PRODUCT OF TWO NONSCALAR ARRAYS
⍝ OF INTEGER POLYNOMIALS.                            
 ⎕IO←1                                               
 DERR∧/(1≤(⍴⍴A),⍴⍴B),(⍴A)[¯1+⍴⍴A]=1↑⍴B               
 C←((RA←¯2↓⍴A),(RB←¯1↓1↓⍴B),1)⍴0                     
 X←1=⍳1↑⍴B                                           
 RR←((⍴RA)+⍳⍴RB),(⍳⍴RA),⍴⍴C                          
 NOTEST←1                                            
LOOP:AX←RR⍉(RB,RA,¯1↑⍴A)⍴X/[¯1+⍴⍴A]A                 
 BX←((¯1↓⍴C),¯1↑⍴B)⍴X⌿B                              
 C←C ZXSUM AX ZXPROD BX                              
 →(∼1↑X←¯1⌽X)/LOOP
∇
==================================================
FUNCTION: ZXPROD
==================================================
∇ C←A ZXPROD B;⎕IO;D                                   
⍝ COMPUTES THE ENTRY-BY-ENTRY PRODUCT OF TWO ARRAYS  
⍝ OF INTEGER POLYNOMIALS.                            
 →NOTEST/BEGIN                                       
 DERR∧/(,A=⌊A),,B=⌊B                                 
 EXPANDV                                             
BEGIN:⎕IO←0                                          
 C←(A∘.×(¯1↑⍴B)⍴1)×((⍳¯1+⍴⍴A),0 ¯1+⍴⍴A)⍉B∘.×(¯1↑⍴A)⍴1
 C←C,((⍴A),¯1+¯1↑⍴A)⍴0                               
 C←+/[¯2+⍴⍴C]((⍴A)⍴-⍳¯1↑⍴A)⌽C                        
 D←1⌈⌈/,+/∨\⌽C≠0                                     
 C←((¯1↓⍴C),D)↑C
∇
==================================================
FUNCTION: ZXSUM
==================================================
∇ C←A ZXSUM B;M;D                                         
⍝ COMPUTES THE SUM OF TWO ARRAYS OF INTEGER POLYNOMIALS.
 →NOTEST/BEGIN                                          
 DERR∧/(,A=⌊A),,B=⌊B                                    
 EXPANDV                                                
BEGIN:M←(⍴A)⌈⍴B                                         
 C←(M↑A)+M↑B                                            
 D←1⌈⌈/,+/∨\⌽C≠0                                        
 C←((¯1↓⍴C),D)↑C
∇
