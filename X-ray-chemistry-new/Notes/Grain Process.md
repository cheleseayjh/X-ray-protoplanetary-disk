## Grain process & protoplanetary disk:

### Paper review:

- From Pro.Du:

  - ```
    尘埃化学的资料
    ```

  - Hasegawa的系列文章 (第一个最基础)
    https://ui.adsabs.harvard.edu/abs/1992ApJS...82..167H/abstract
    https://ui.adsabs.harvard.edu/abs/1993MNRAS.261...83H/abstract
    https://ui.adsabs.harvard.edu/abs/1993MNRAS.263..589H/abstract
    其中也包含化学反应列表

    也可参考
    https://ui.adsabs.harvard.edu/abs/1982A%26A...114..245T/abstract

    也可参考Tielens的书4.2节

    还可参考毕业论文
    http://hss.ulb.uni-bonn.de/2012/2949/2949.pdf

    关于具体的尘埃化学反应网络可参考
    http://hosting.astro.cornell.edu/~rgarrod/resources/

    我也有自己从文献中整理出的化学反应组成的反应文件；如果只需要H2O等少数分子相关的反应网络的话，从文献中搜集的工作量不会很大

- Hasegawa, 1992

  - 对存在dust的molecular cloud，dust上物质浓度变化：

    ​		挥发（desorption）的过程只有热运动导致的脱离——还没有完整的理论能很好的解释现象

    ​						一种说法：表面放热反应作为

    ​		吸收（absorption）过程有两种，i. ion-molecule reaction in gas，然后通过吸积作用附着到dust上

    ​																 ii. direct surface reaction，直接在表面发生反应——有证据表明																	 比H2复杂的分子可以在部分表面上直接形成

  - 对分子浓度的影响：

    - 对 hot core source in Orion，观察到大量H2O,NH3，从而存在 ion-molecule 以外的反应机理，

      热挥发的 H atom 导致的表面氢化作用（Surface hydrogenation）是其中一种

    - Tielens & Hagen, 1982：从一个 **gas-phase稳定模型+large grain** 开始分析，重分子不易发生desorption，从而会积累在large grain上；同时轻元素H、C、N、O会主导迁移过程（dominate surface migration chemistry）而维持其在 gas 中的浓度

      Tielens & Allamandola, 1987：另一个模型中为了保持模型丰度稳定，引入了 grain explosion （小的grain还是可以发生这个过程的）与 photodesorption 过程，相当于增加了从 grain 到 gas 的转移，同时对有机分子进行光破坏来增加小分子浓度（对应photodesorption）

    - Another view（Brown, 1990）：利用放热反应的能量，重自由基也可以发生迁移并且参与到更多的 gas 反应之中（只有在 gas 里它们才能相遇），e.g.：

    $$
      CH_3 \quad + \quad OH \quad \xrightarrow{energy} \quad CH_3OH
    $$

      在这样的观点下，grain 对于可能发生的反应的限制就没有那么强（原先认为重自由基之间无反应）

  - 吸积作用（nonthermal desorption）对演化体系时间尺度上的影响：

    - 对稳定系统（$t > 1\times 10^7 yr$）没有什么意义，因为到达稳定状态需要的时间太长了

  - 对早期演化（$10^5 \sim 10^6 yr$）也没有太大影响——By Brown&Charnley, 1991

  - Hesegawa model 的基本考虑：

    - 尝试针对有机物丰度在 grain 上的急剧增加构建反应网来说明

    - 出发点：Herbst & Leung, 1989 &1990 关于纯气相的大型反应网，考虑 dark cloud（no heating）

      加入一系列 grain-surface reaction ，直至10原子分子参与的反应

    - Restrictions：采用TH & TA 的观点，即重分子沉积在 grain 上，相互之间的反应很少

      ​						 **没有考虑 nonthermal desorption**（e.g. photodesorption）

    - **没有离子吸积**，即没有考虑电荷问题

  - **<u>Parameter</u>**

    - clasical dust grains:  radius=1000 Å ,  density=3 g/cm^3 ,   surface sites=10^6
    - gas-to-dust ratio (on mass):  100 
    - number density of grains=1.33 * 10^(-12)
    - temperature=10 K



- **Surface reaction rate coefficient**

  - enviroment:	
    $$
    \text{grains —— number density  }n_d=1.33\times 10^6 n_H \\
    \text{surface sites on }\textbf{a grain —— }N_s=10^6 \\
    \text{surface sites number density —— }n_s=1.5\times10^{15}\text{cm}^{-2}
    $$
    ​	Reactions could only occur when molecules on **the same grain**

  

  - migration time :
    $$
    \text{potential between surface sites —— }E_b \\
    \text{adsorption energy —— }E_D \\
    \text{characteristic vibration frequency for adsorbed species —— }\nu_0=\sqrt{\frac{2n_s E_D}{\pi^2 m}}
    $$

    $$
    t_{hop} = \nu_0^{-1}\exp(\frac{E_b}{kT_d})
    $$

    ​	Since the probability for migration to each site on the grain is equal, time for destination-limited migration —— the diffusion time is:
    $$
    \text{diffusion time —— }t_{diff}=N_s t_{hop} \\
    \text{diffusion rate —— }R_{diff}=\frac{1}{t_{diff}}
    $$

  - surface reaction rate :

    ​	Surface reaction rate between species *i, j* could be calculated by giving the frequency of encounters on an average grain and probability for reaction upon an encounter.

    ​	For details, we can calculate diffusion rate for species i, j ,respectively. The sum would be our result.
    $$
    \text{probability for reaction upon an encounter —— }\kappa_{ij} \\
    \text{nubers of molecules of species i on an average grain —— }N_i \\
    \text{surface reaction rate —— }R_{ij} \\
    \kappa_{ij}=\exp[-\frac{2a}{h}\sqrt{2\mu E_a}] \\
    R_{ij}=\kappa_{ij}(R_{diff,i}+R_{diff,j})N_i N_j n_d \equiv k_{ij}(N_i n_d)(N_j n_d)
    $$
    ​	Thus, the rate coefficient is:
    $$
    k_{ij}=\frac{\kappa_{ij}(R_{diff,i}+R_{diff,j})}{n_d}
    $$

  - special case :

    ​	For H and H_2, **quantum tunneling dominates** the migration process. Use this time scale to replace the old t_hop.
    $$
    t_q=\nu_0^{-1}\exp[\frac{2a}{h}\sqrt{2mE_b}] \\
    R_{diff'}=\frac{1}{N_s t_q}
    $$



- **Accretion process**

  - accretion rate for species i :
    $$
    R_{acc}(i)=\sigma_d \overline{v(i)}n(i)n_d \\
    k_i=\sigma_d \overline{v(i)}n_d
    $$

- Hasegawa, 1993

  - hydrogenation reactions on surface
    $$
    \text{hydrocarbons —— }C_n,\space C_nH\\
    C_n+H_2\rightarrow C_nH+H \\
    C_nH+H_2\rightarrow C_nH_2+H
    $$
    ​	**if activation energy barries are sufficiently low**, these reactions can occur at appreciable rates due to tunneling.

    （但从表中给出的系数来看，量级1E-01~1E-05和已加入的反应量级1E+12差的似乎很远）

    

  - CR induced desorption

    ​	In CR, *relativistic Fe nuclei (20-70MeV) deposit 0.4MeV into dust particles*. In all, <u>impulsively heating V.S. cooling via thermal evaporation & radiation</u>.

    ​	We derive **the time spent by grains in the vicinity of 70K *f(70K)***	and we get:

$$
    k_{crd}(i)=f(70K)k_{evap}(i,70K)=3.16\times10^{-19}\nu_i \exp[-\frac{E_D(i)}{70K}]
$$

    	量级大约 < 1E-10


​    

  - three-phase —— *adding dust particle mantles*

    ​	consider a group of dust particles, the mantle part (inside, non-surface dust particles) should be reaction-inactive —— different from previous consideration.

    ​	further thinking of migration among dust particles —— mantle & surface

    ​	NEED FURTHER INVESTIGATION



- K.Willacy 1998 —— a disk with central star and high temperature (total different model from us!!)

  ​	mentioned Aikawa et al. (1997) —— a star at center, with **CR ionization** & freeze-out & thermal desorption & NO mantle phase

  ​	Result —— CR is important to destroy CO & N2 ；abundance varies considerably with distance from central star

  - Model :

    ​	a central star, region of disk between 0.1AU-100AU, high temperature

    ​	gas-grain interaction, freeze-out, desorption, grain mantle chemistry



- Walsh, Millar 2010 —— chemical processes in protoplanetary disks

  - photodesorption:

    ​	non-theoratical, indiscriminate based on experimental results

    ​	suggest <u>each photon</u> absorbed by *grain mantle* returns a <u>particuler number of molecules</u>. （不同种类分子desorption的概率相同）

    ​	Thus, **desorption rate depends on fractional abundance**.
    $$
    k_i^{pd}=k^{pd}\frac{n_i^s}{n_{tot}^s}=F_{UV}Y_{UV}\sigma_d x_d\frac{n_i^s}{n_{tot}^s}
    $$

  - X-ray desorption:

    ​	use same consideration as above.

    ​	*But there should be ionization, etc.—— Unreasonable*



- R.Visser et al. , 2011

  - gas-grain interaction by UV:

    ​	mentioned about H2O ice, but ignored the effect because it is non-trivial task.

    ​	Then get UV-inducing desorption rate:
    $$
    \pi a_{gr}^2 —— \sigma_d \\
    n_{gr} —— \text{grain number density}\\
    f(X)\approx \frac{n(X)}{n_{total}}\\
    Y(X)\approx 10^{-3}\\
    F_0 —— \text{UV flux}\\
    \tau_{UV,eff} —— \text{effective UV extinction}
    $$
    
    $$
    R_{phdes}(X)=\pi a_{gr}^2n_{gr}f(X)Y(X)F_0\exp(-\tau_{UV,eff})
    $$
    ​	Note that confliction between R.Visser's paper and Walsh's paper does not exist.

    



### Main considerations:

- **Accretion**

  - accretion rate for species i :
    $$
    R_{acc}(i)=\sigma_d \overline{v(i)}n(i)n_d \\
    k_i=\sigma_d \overline{v(i)}n_d=\pi a^2 \sqrt{\frac{k_B T_g}{m_i}}\space n_d
    $$


- **Surface reaction**

  - migration time :
    $$
    t_{hop} = 
    \left\{
    \array{\nu_0^{-1}\exp[\frac{2a}{h}\sqrt{2mE_b}] \hspace{0.5cm} H/H_2\\ \nu_0^{-1}\exp(\frac{E_b}{kT_d})\hspace{0.5cm} \text{ other species}}\right.
    $$

  - surface reaction rate :
    $$
    R_{diff}=\frac{1}{N_s  t_{hop}} \\
    \kappa_{ij}=\exp[-\frac{2a}{h}\sqrt{2\mu E_a}] \\
    k_{ij}=\frac{\kappa_{ij}(R_{diff,i}+R_{diff,j})}{n_d}
    $$

- **Desorption**

  - thermal desorption :
    $$
    k_{evap}(i)=\nu_0\exp(-\frac{E_D}{kT_d})
    $$

  - CR desorption:
    $$
    k_{crd}(i)=f(70K)k_{evap}(i,70K)=3.16\times10^{-19}\nu_i \exp[-\frac{E_D}{70K}]
    $$

  - Photodesorption:
    $$
    R_{phdes}(X)=\pi a_{gr}^2n_{gr}f(X)Y(X)F_0\exp(-\tau_{UV,eff})
    $$
  
  - X-ray desorption:
  
    ​	Neither theoretical analysis nor observational result can be found...



