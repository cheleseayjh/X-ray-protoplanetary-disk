# Documentation for KROME & X-ray project

This project is aiming to analyze X-ray chemistry in protoplanetary disk , using *astrochemistry* package `KROME` to do all our simulations. The document here , written by Jianghui Yu , concludes the set-ups of Jianghui Yu & Chang Liu's previous work (under the supervision of Prof. Xian Chen and Prof. Fujun Du).



Our project has been uploaded to Github : [cheleseayjh](https://github.com/cheleseayjh)/**[X-ray-protoplanetary-disk](https://github.com/cheleseayjh/X-ray-protoplanetary-disk)** 

## brief introduction to KROME

- official website : https://bitbucket.org/tgrassi/krome/wiki/Home , but it has little useful things

- need Linux or OS ; Python 2.7 (Python 3 is not supported)

- Here is a documentation done by Chang Liu, showing the logic of KROME as well as necessary files in KROME package , which will be used frequently in our simulation. Please make sure you have read it carefully and successfully install KROME on your Linux / OS system :

  ​	https://github.com/slowdivePTG/X-ray-chemistry/blob/master/KROME_documentation.md





## simulation for molecular cloud model

​	first give an introduction on X-ray chemistry & grain model , then discuss our simulation method (including KROME & external control system) , finally give some important details you need to change on your own laptop.

### chemical theory :

​	molecular cloud -- formed by interstellar gas & dust grains . We need to construct a gas-grain model , adding X-ray effect on it.

​	for radiation field , consider CR & UV & X-ray , see Chang's paper or mine.

- X-ray chemistry -- ionization on atoms

  ​	since we consider cold-neutral molecular cloud , we <u>ignore X-ray heating effect</u> , considering ionization ;

  ​	theory of X-ray ionization on grain surface remains unknown , and it might be a rather small effect , so <u>just considering ionization in gas</u> ;

  ​	due to some theories , we've added several ionization reaction on atoms , considering **both primary & secondary ionization for H, He and only secondary ionization for other atoms** 

  - dealing with X-ray in KROME : 

    ​    since the shape of X-ray spectrum takes little difference , we fixed a power law spectrum , using ONE parameter `J21xray` to control the total flux , you can set it in `test.f90` .

    ​	opacity should be considered , and here we need to **calculate column density of H** , denote as $ncol_{H}$ . 

  - Ref : 

    - my note : 

      https://github.com/cheleseayjh/X-ray-protoplanetary-disk/blob/master/X-ray-chemistry-new/Notes/The%20Way%20KROME%20Calculates%20'auto'%20Ionization%20Rates.md

    - Latif's paper : 

      https://ui.adsabs.harvard.edu/abs/2015MNRAS.446.3163L/abstract

- grain model

  ​	we have two phases in our system -- gas phase & grain phase , thus there should be 4 interactions:

  1. reactions in gas phase -- we will directly adopt a model and add our X-ray consideration

  2. molecules from gas to grain -- accretion process

     ​	when molecule in gas meets dust grain , it will settle on grain surface.

     ​	accretion rate for species i :
     $$
     R_{acc}(i)=\sigma_d \overline{v(i)}n(i)n_d \\
     k_i=\sigma_d \overline{v(i)}n_d=\pi a^2 \sqrt{\frac{k_B T_g}{m_i}}\space n_d
     $$

  3. molecules from grain to gas -- desorption process

     ​	three desorption channels

     - thermal desorption -- surface molecule satisfies Boltzmann distribution might escape from grain surface
       $$
       k_{evap}(i)=\nu_0\exp(-\frac{E_D}{kT_d})
       $$

     - CR desorption -- cosmic-ray striking grain , gives a sudden high temperature , causing desorption effect
       $$
       k_{crd}(i)=f(70K)k_{evap}(i,70K)=3.16\times10^{-19}\nu_i \exp[-\frac{E_D}{70K}]
       $$

     - photo-desorption -- UV strikes grain , only observational evidence but no theory right now , giving an empirical eq.
       $$
       R_{phdes}(X)=\pi a_{gr}^2n_{gr}f(X)Y(X)F_0\exp(-\tau_{UV,eff})
       $$

  4. reactions on grain surface -- grain surface reaction

     ​	when molecules settle on grain , they cannot meet with each other. So we assume a potential barrier and molecules may migrate due to kinetic motion. We calculate migration time —> migration rate —> reaction rate
     $$
     t_{hop} = 
     \left\{
     \array{\nu_0^{-1}\exp[\frac{2a}{h}\sqrt{2mE_b}] \hspace{0.5cm} H/H_2\\ \nu_0^{-1}\exp(\frac{E_b}{kT_d})\hspace{0.5cm} \text{ other species}}\right.
     $$

     $$
     R_{diff}=\frac{1}{N_s  t_{hop}} \\
     \kappa_{ij}=\exp[-\frac{2a}{h}\sqrt{2\mu E_a}] \\
     k_{ij}=\frac{\kappa_{ij}(R_{diff,i}+R_{diff,j})}{n_d}
     $$

  - Ref :

    - Hasegawa's papers (see 1992 first):

      https://ui.adsabs.harvard.edu/abs/1992ApJS...82..167H/abstract
      https://ui.adsabs.harvard.edu/abs/1993MNRAS.261...83H/abstract
      https://ui.adsabs.harvard.edu/abs/1993MNRAS.263..589H/abstract

    - my note :

      https://github.com/cheleseayjh/X-ray-protoplanetary-disk/blob/master/X-ray-chemistry-new/Notes/Grain%20Process.md

### KROME simulation & external control

​	reminder : our code on Github is partly copied from your local KROME package , and partly our controlling code

- KROME's logic :

  1. choose network

     our network on Github : `./KROME/AGN_pc_yjhtest/x`

     https://github.com/cheleseayjh/X-ray-protoplanetary-disk/blob/master/X-ray-chemistry-new/KROME/AGN_pc_yjhtest/x

     - gas phase 

       Wakelam, 2008 (it is in your KROME package,`./krome/network/reaction_cloud`) + X-ray ionization reactions

     - grain phase

       our code is on Github : `./KROME/AGN_pc_yjhtest/Grain Process.ipynb`

       https://github.com/cheleseayjh/X-ray-protoplanetary-disk/blob/master/X-ray-chemistry-new/KROME/AGN_pc_yjhtest/Grain%20Process.ipynb

  2. write information in your network into `./krome/build/subs.f90` , prepare related physical module (we don't know the details, yet we don't have to)

     important information usually in `subs.f90` `ode.f90` `getphys.f90`

  3. run `./test` , i.e. input `test.f90` to your command , do chemical evolution , finally get your result

  

  KROME's problem

  ​	when run `./test` , KROME will **overwrite your `test.f90` `ratexH.dat` `ratexHe.dat` etc.** and bring a lot of difficulties , which makes us not able to change our physical & chemical model.

- external control & **standard code-running method** 

  1. run your own KROME until having done `make gfortran` , but have not done `./test` , for example :

     ```fortran
     ./krome -project=your_project -n=networks/your_network -noRecCheck
     
     ...
     
     make gfortran
     ```

  2. use our controlling code to rewrite `test.f90` `getphys.f90` etc.

     ​	detailly speaking , first copy your local `./krome/build` to your Python project (my project is `AGN_pc_yjhtest` on Github) , then run `AGN.ipynb`.

     ​	it will rewrite `test.f90` to simulate different circumstances , and fix relating details.

  3. you will get the result from simulation

     by the way , you can encode your own controlling code to satisfy your requirement , our `AGN.ipynb` is a good example.

### important details

​	really need your double check !

​	after copied to your Python project , check your files in Python project by following steps :

- X-ray ionization reaction (see `AGN_pc_yjhtest/subs.f90` as an example)

  ​	our chemical network including only ionization of H & He , and secondary ionization rate has been calculated in `ratexH.dat` `ratexHe.dat` . 

  ​	so first open `subs.f90` and replace `k(4430), k(4431)` by :

  ```fortran
      !H -> H+ + E
      k(4430) = small + ratexH * J21xray
  
      !HE -> HE+ + E
      k(4431) = small + ratexHe * J21xray
  ```

  ​	then add other reactions directly to `subs.f90` , like :

  ```fortran
      !CO -> C + O
      k(31) = k(31) + 4.7093110781728 * k(4430)*0.8
  
      !CO -> CO+ + E
      k(32) = k(32) + 4.7093110781728 * k(4430)*0.2
  ```

- `ode.f90` 

  if there are two `dn(idx_H)` , you should put the two parts together (since then it gives the exact value)

- column density

  ​	we do not use the `num2col` function to get column density , instead we calculate by ourselves. 

  ​	thus in `AGN.ipynb` we change its function in `getphys.f90 `: 

  ```python
  def AGN(...):
  	...
      with open('krome_getphys.f90', 'r') as f:
      lines = f.readlines()
      lines[3715] = 'num2col = max(ncalc,1d-40)*{}\n'.format(str(NH / 2e4))
      ...
  ```

  ​	Remember , **the number 3715 here might change** after your compiling , please check your `getphys.f90` to find the correct line number !

- network `react_cloud` & our `x` 

  ​	in gas phase , Wakelam 2008 denote as

  ```fortran
  CH4O,CH4O+;C2H2N,C2H2N+;C2H3N,C2H3N+
  ```

  ​	but in our `Grain Process.ipynb` , the corresponding species denoted as

  ```fortran
  CH3OH,CH2CN,CH3CN ; CH4O+,CH2CN+,CH3CN+
  ```

  ​	thus we should unify them. the version of `./KROME/AGN_pc_yjhtest/x` is correct.

### plot issue

​	just see `AGN_plot.ipynb` (https://github.com/cheleseayjh/X-ray-protoplanetary-disk/blob/master/X-ray-chemistry-new/KROME/AGN_pc_yjhtest/AGN_plot.ipynb)





## simulation for protoplanetary disk

​	first gives an introduction to protoplanetary disk & method of chemical evolution simulation , then discuss our code on Github , finally point out remaining problems.

### protoplanetary disk

- formation & structure

  ​	formed by gravitational collapse of molecular cloud

  ​	a protoplanetary disk including central star & surrounding gas and grain

  - Ref :

    - Jonathan's review : 

      https://ui.adsabs.harvard.edu/abs/2011ARA%26A..49...67W/abstract

    - my note : 

      https://github.com/cheleseayjh/X-ray-protoplanetary-disk/blob/master/X-ray-chemistry-new/Notes/Protoplanetary%20disk.md

- evolution

  ​	usually separated to physical evolution & chemical evolution , yet nobody successfully combined them together.

  ​	since we're interested in chemical evolution , we just simply **fix physical structure** , than do chemical evolution at each spatial point , choose a uniform time to print our abundance distribution as our result (known as **pseudo-time analysis**).

  - physical structure -- use analytical model

    ​	these models are all axial symmetric disk , i.e. 2D model . 3D is too complicated to simulate

    density structure : 
    $$
    \rho_{\text{H}} (R,\Theta) \approx \rho (R,\Theta) = \frac{\Sigma}{\sqrt{2\pi} R h} \exp{\left[ -\frac{1}{2} \left( \frac{\pi / 2 - \Theta}{h} \right)^2 \right]}
    $$
    ​	and we have
    $$
    \Sigma = \Sigma_c \left( \frac{R}{R_c} \right)^{-\gamma} \exp{\left[ -\left( \frac{R}{R_c} \right)^{2-\gamma} \right]}
    $$

    $$
    h = h_c \left( \frac{R}{R_c} \right)^{\psi}
    $$

    temperature structure : 
    $$
    T = T_c \left( \frac{R}{R_c} \right)^{-q}
    $$
    column density : 

    ​	contributed ONLY by protoplanetary disk , just simply integrate $n_{\text{H}}$ 

    - Ref : Andrews's paper

      https://ui.adsabs.harvard.edu/abs/2009ApJ...700.1502A/abstract

  - radiation field

    ​	for now we neglect radiation from central star (because we haven't add it) , thus we can only study outer disk ($R\geq 100\text{AU}$).

    ​	for AGN radiation , use previous data.

  - chemical network

    ​	still use `x` , but obviously it lack of heating & cooling process ; for outer disk it works due to disk temperature $T<15\text{K}$ , but ultimately we need to study the inner region .

    ​	thus heating & cooling part is necessary , you may get some idea in `getphys.f90` and the examples in your local `./krome/test` (i.e. how to write `test.f90` to include heating part , etc.)

  - radiation transfer & non-axisymmetric model

    ​	radiation (e.g. X-ray) may be attenuated by gas in the disk (as we consider column density here) , thus we get a non-uniform external radiation field.

    ​	if radiation does not irradiate face-on disk , it will **break axial symmetry** when adding radiation flux to our disk structure data . thus **2D model no longer works and we need to find a proper way to simplify 3D model** , that is the important part.

    ​	we have no idea about it now. as for a try , we calculate only the line along radiation direction and cross central star : 

    <img src="C:\Users\41-巴巴罗萨\AppData\Roaming\Typora\typora-user-images\image-20201031211913990.png" alt="image-20201031211913990" style="zoom:45%;" />

### simulation

​	code is in `Diskstructure.ipynb` , with necessary details in it. if you have successfully done `AGN.ipynb` , this will not be a burden for you.

​	for plot issue , see `AGN_plot.ipynb` , we have enough illustration there and you can compare those functions to each other for getting your own code.

### remaining problems

- grain model , especially desorption analysis

  - Ref : Shalabiea's paper

    https://ui.adsabs.harvard.edu/abs/1994A%26A...290..266S/abstract

- X-ray heating effect

- heating & cooling theory in protoplanetary disk and encoding method

- non-axisymmetric disk modelling method

- ...

