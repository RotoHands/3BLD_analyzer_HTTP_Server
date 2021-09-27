# UPDATE - 2021-09
#### This is a HTTP server that can get Rubiks blindfolded solves and return them analyzed
#### check Client_Example.html to see the format of the fetch request.
[TrainBLD.com](https://www.trainbld.com/) - [github repo](https://github.com/RotoHands/TrainBLD)  check the web timer I developed to show Proof Of Concept for using this HTTP server

If you are a webtimer develooper and you need help to implement this feature feel free to contact - Rotohands@gmail.com

### Reconsruction features
- commutator seperation
- letter pair
- move count
- time per alg
- memo time
- exe time
- fluidness ((exe time - pauses)/exe time)
- added time per alg
- added solve description : 12'/8'' - (12) edge targets, (') flipped edge / (8) corner targets, ('') 2 corner twists
- can send both txt analysis and link to cubeDB


### Example solve - smart cube (UF, UFR, Speffz)
[cubeDB](https://www.cubedb.net/?puzzle=3&title=14%2F9_35.97%25280.44%2C35.53%2529__51.51%25%0A9%2F27%2F2021%2C_01%3A35_PM&scramble=F2_L2_U_B2_U-_F2_U_L-_D-_B_R_F-_R_U-_F2_R-_B-_R_B_D-_R2_U_B_&time=35.53&alg=%2F%2Fedges%0AR-_U-_R2_S_R2_S-_U_R_%2F%2F_JA__8%2F8__1.74%0AU-_R_E-_R-_U_R_R-_R_E_R-_%2F%2F_BH__10%2F18__1.08%0AL_F_L-_E_L_F-_L-_E-_%2F%2F_PL__8%2F26__0.88%0AL_F-_E_R2_E-_R2_F_L-_%2F%2F_NU__8%2F34__1.23%0AS_L-_F-_L_S-_L-_F_L_%2F%2F_VG__8%2F42__1.89%0AU2_R-_E_R_U_R-_E-_R_U_%2F%2F_FD__9%2F51__0.75%0AL_F-_L-_S-_L_F_L-_S_%2F%2F_EB__8%2F59__1.48%0A%0A%2F%2Fcorners%0AU_R-_D_R_U-_R_D-_R-_U-_R_D_R-_U_R-_D-_R_%2F%2F_VB__16%2F75__1.39%0AF-_U_R-_D-_R_U2_R-_D_R_U_F_%2F%2F_LN__11%2F86__1.92%0AU-_R-_U-_R-_D-_R_U_R-_D_R2_U_%2F%2F_DR__11%2F97__1.52%0AR_U_R_U_R-_D2_U-_U_R_U-_R-_D2_U-_R-_%2F%2F_TX__14%2F111__2.11%0A%0A%2F%2Fparity%0AR2_D_R-_U2_R_D-_R-_U-_R-_F-_R_U_R-_U-_R-_F_R2_U-_R-_U-_%2F%2F_CB_CI__20%2F131__2.31%0A)
<details>
  <summary>unparsed</summary>

<p>
F2 L2 U B2 U' F2 U L' D' B R F' R U' F2 R' B' R B D' R2 U B  //scramble

R' U' R' R' F' B U U B' F U R U' R U' D B' U B B' B D' U R' 
L F L' U D' B L' B' D U' L F' D' U F' F' D U' R R F L' B F'
D' F' D B' F L' F L U U R' U D' F U F' D U' R U L F' L' B' 
F U F U' B F' U R' D R U' R D' R' U' R D R' U R' D' R F' U
R' D' R U U R' D R U F U' R' U' R' D' R U R' D R R U R U R
U R' D D U' U R U' R' D D U' R' R R D R' U U R D' R' U' R' 
F' R U R' U' R' F R R U' R' U' //solve
</p>
</details>

<details>
  <summary>parsed</summary>


14/9 35.97(0.44,35.53)  51.51%

F2 L2 U B2 U' F2 U L' D' B R F' R U' F2 R' B' R B D' R2 U B //scramble

//edges  
R' U' R2 S R2 S' U R // JA  8/8  1.74
U' R E' R' U R R' R E R' // BH  10/18  1.08  
L F L' E L F' L' E' // PL  8/26  0.88  
L F' E R2 E' R2 F L' // NU  8/34  1.23  
S L' F' L S' L' F L // VG  8/42  1.89  
U2 R' E R U R' E' R U // FD  9/51  0.75  
L F' L' S' L F L' S // EB  8/59  1.48  

//corners  
U R' D R U' R D' R' U' R D R' U R' D' R // VB  16/75  1.39  
F' U R' D' R U2 R' D R U F // LN  11/86  1.92  
U' R' U' R' D' R U R' D R2 U // DR  11/97  1.52  
R U R U R' D2 U' U R U' R' D2 U' R' // TX  14/111  2.11  

//parity  
R2 D R' U2 R D' R' U' R' F' R U R' U' R' F R2 U' R' U' // CB CI  20/131  2.31
 
</details>

for more information check this [post](https://www.speedsolving.com/threads/smart-cube-bld-analyzer.84773/)

P.S
Thanks for [CSTIMER](https://github.com/cs0x7f/cstimer/blob/fc627f0970d8982c758200430bb60d7554f984b0/src/js/bluetooth.js) for the bluetooth implementation for smart cubes



# Original - 2021-06
Hi,
After [last year](https://www.speedsolving.com/threads/3bld-dnf-analyzer-new-software-i-made.76945/) software attempt of making a more efficient way to train 3bld, here is this year version!
I worked on a new version for the last couple of months and focused mainly on analyzing 3bld solves.

main features:
- separating the solve commutators
- tracking the commutator and converting to letter pairs
- converting parallel layers to slice moves
- customizable letter pairs
- customizable buffers
- recognize twist, flips and cycles outside the buffer
- recognize mistakes in solve, points to last place execution was right  
- expand commutators to their full alg, after cancelling moves
- compatible with solves from cubedb.net and alg.cubing.net
- can generate url link to cubdb.net
- works on 3style, M2, OP

[github repo](https://github.com/RotoHands/3BLD_parser)
### example solve - smart cube (UF, UFR, Speffz)
<details>
  <summary>unparsed</summary>

<p>
R2 U' B2 F2 L2 U' R2 D F2 U2 B2 R' D' L' D F' D2 B2 D2 L2 //scramble

U' F' B U B U' F B' R B' R' U U' D R' U' D B B U D' R' U D' 
R U' R' U D' F U F' U' D R' F R F' B U' U' F B' R F' R U' U'
L D U' F' U' F U D' L' U' U D' F U' D R' U' R U D' F' D R F' 
L' F R' L D' L D L' D' L' D R L' F' L F R' L U' D' R' U U R'
D R U U R' D' R2 U D D R U R' D R U' R' D D R' U R' D' R U 
U R' D R U R R' D' R D R' D' R U U R' D R D' R' D R U U
</p>
</details>

<details>
  <summary>parsed</summary>

<p>
R2 U' B2 F2 L2 U' R2 D F2 U2 B2 R' D' L' D F' D2 B2 D2 L2 //scramble

//edges  
U' S R B R' S' R B' R' U // SQ   10/10   
U' D R' E' R R E R' U D' // UR   10/20   
R U' R' E R U R' E' // JF   8/28   
R' F R S R' R' S' R F' R // EO   10/38   
U' U' L E' L' U' L E L' U' // PB   10/48   
E R E' R' U' R E R' D y // TB   9/57   
R F' L' F M' F' L F L' x' // KG   9/66   
D' L' D M D' L D M' // HK   8/74  
  
//corners  
U' D' R' U U R' D R U U R' D' R2 U D // VN   15/89   
D R U R' D R U' R' D D // LH   10/99   
R' U R' D' R U U R' D R U R // OF   12/111   
R' D' R D R' D' R U U R' D R D' R' D R U U // CA twist   18/129   
</p>
</details>

### A bit more details
checkout this [post](https://www.speedsolving.com/threads/smart-cube-bld-analyzer.84773/)
