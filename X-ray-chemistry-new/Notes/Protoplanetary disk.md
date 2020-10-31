## Protoplanetary disk

- [Review] Protoplanetary disks and their evolution, 2011

  ​	In general, it focused on properties and evolution of outer part (beyond 1AU) around low-mass star

  

  - formation & basic information
  
    - enviroment --> central star --> disk (angular momentum conserved)
  
      star formation period (before disk) ~ 0.5Myr , rather short
  
    - radius —— around 10^1 ~ 10^2 AU (to magnitude accuracy)
  
    - surface density (beyond 20AU) :
      $$
      \text{mass density about surface }\rho\propto R^{-\gamma}(\gamma\in [0,1])
      $$
  
    - $$
      \text{total mass }\thicksim 5 M_{jup}\thicksim 0.005 M_{\odot}
      $$
  
    - structure —— flared (intercept and reprocess more stellar radiation)
  
    
  
  - composition
  
    - dust —— mainly silicates with sizes r < 0.1μm 
  
      ​	general process include <u>molecules freeze out, grain collision, etc.</u>
  
    - gas —— 99% of total mass (**corresponding to our gas-to-dust ratio**)
  
    
  
  - evolution
  
    - photoevaporation by central star —— models
  
      1. focus on EUV (1994-2006) . heating H2 , time-scale with considering viscosity
  
         *restrict to inner part*
  
      2. recently include X-ray (Owen et al.2010) . penetrate neutral gas & influence larger radii (~tens of AU)
  
      3. diffence between X-ray + EUV model  &  EUV only model (Armitage 2011)
  
         100 times photoevaporation rate
  
    - photoevaporation from nearby stars :
  
      ​	erode outer part of disk ; leave < 50 AU inner part
  
    - important grain process —— grain growth & dust settling
  
      - grain growth :
        $$
        \text{grain stick together }\rightarrow \text{drop into midplane }\rightarrow \text{increase inner density}
        $$
        related to planet formation (**time-scale** is very important now)
  
      - dust settling :
  
        ​	reduce the height & flaring angle of disk (i.e. settle vertically)
  
      
  
    - picture of evolution steps : 
  
      ![image-20200515220549198](C:\Users\41-巴巴罗萨\AppData\Roaming\Typora\typora-user-images\image-20200515220549198.png)
      
      ![image-20200516090125005](C:\Users\41-巴巴罗萨\AppData\Roaming\Typora\typora-user-images\image-20200516090125005.png)





- **Possible consideration**

  - time-scale

    ​	our typical chemical evolution time-scale is about 1Myr

    ​	disk evolution time-scale is about 0.1Myr ~ 10Myr (to many aspects), which may influence grain density, temperature, etc.

    ​	it's necessary to pay attention to time-scale of evolutional process



- Walsh 2012

  - Physical model

    ​	accretion disk model —— requiring central star's *mass, radius, disk accretion rate*

    ​	radiation from inner star —— X-ray & FUV (mainly)

    - Central star information
      $$
      \text{mass: }M_{*}=0.5M_{\odot} \\
      \text{radius: }R_*=2R_{\odot} \\
      \text{temperature: }T_*=4000K
      $$

    - UV radiation field (unimportant)

      - from central star:
        1. blackbody spectrum
        2. hydrogenic bremsstrahlung emission (轫致辐射)
        3. strong Lyα line emission

    - X-ray radiation field (*from central star*) information
      $$
      \text{luminosity: }L_X\sim 10^{30}\text{erg/s} \\
      \text{hydrogen column density: }N_H=2.7\times10^{20}\text{cm}^{-2}
      $$
      ​	extinction —— ionization in gas & compton scattering by hydrogen

      ​	e.g. X-ray spectrum at 56pc:![img](file:///C:\Users\41-巴巴罗萨\Documents\Tencent Files\744943491\Image\C2C\_[EM03M$H0%_P3YLEL6]HXG.png)

    - Disk physics structure

      <img src="C:\北大文件\本科生科研\paper research of Protoplanetary Disks\physics structure.png" alt="physics structure" style="zoom:150%;" />

      ​	(Z/R —— disk height/disk radius; density —— total gas density)

      1. <u>**comparing to our X-ray flux (>1e-3)**</u>: focus on >10AU
      2. UV vanished
      3. temperature < 50K

  

  - Chemical consideration (we have also considered)

    - gas phase —— http://www.udfa.net (Woodall et al. 2007) for dense cloud

    - gas-grain interaction (ref Hasegawa):

      - gas accretion

      - desorption

        1. thermal desorption

        2. CR desorption

        3. photodesorption (UV) (Westley et al. 1995; Oberg et al. 2007; Willacy 2007)

           ​	change the rate coefficient parameter <u>due to different grain mantle composition</u>

      - grain-surface network

    - initial abundance

      ​	from dark cloud model (oxygen-rich, low-metal)
      $$
      T=10\text{K}\hspace{0.5cm}n(H_2)=10^4 \text{cm}^{-3}\hspace{0.5cm}A_V=10 \text{ mag}
      $$
      ​	<u>use data at 1e5 yr</u> as initial condition

  

  - Chemical consideration (we didn't consider)

    - photochemistry (caused by UV)

      ​	for us, not important when radius >100AU

    - X-ray ionization

      1. use <u>true energy spectrum instead of power-law fit spectrum</u>
      2. add direct X-ray ionization (??)

  

  - Evolution

    ​	consider chemical network evolution, <u>seems including disk evolution</u> 

    ​	<u>display result at 1e6 yr</u>

  

  - Result (see figures)

    - photochemistry is important, rather than X-ray ionization (~10AU)

    - N2H+ is the only molecule especially affected by X-ray

      ​	this can be detected along with CO, etc.