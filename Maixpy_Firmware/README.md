# K210 Firmware

## 1. Introduction of Firmware

k210在实现代码前必须烧入固件。官方提供了多种类型的固件，它们根据所支持的功能有不同的名称格式，*readme.txt* 中有各个类型所支持的功能，在熟练后根据自己的需求下载。

在 *Maixpy_Firmware* 文件夹中，我放入了在开发过程中所使用过的三种固件，版本为写 *README.MD* 的最新版本，在 Witdog 上烧入的固件是maixpy_v0.6.2_84_g8fcd84a58_openmv_kmodel_v4_with_ide_support。

## 2. Troubles about Firmware
在这里将总结笔者在 K210 开发过程中有关固件所遇到的问题，希望后续开发者不要踩坑。

- 在初次往 K210 里面烧入固件时，直接使用完整版固件可以避免很多问题。
- 当你不小心烧错固件时，直接将正确固件烧入 K210 可以解决一半情况下的问题。但是如果烧完以后屏幕出现蓝屏、白屏等问题或者代码无法运行，就需要擦除 flash 了，擦除的方法如下图所示。事实上，更改固件的标准流程就是先将 flash 擦除，再烧入新的固件，但是实际操作上同种类型的固件只需要将新的固件烧入即可。

<div  align="center">    
    <img src="https://github.com/zgchen33/witdog_ros/raw/K210/image/cachuflash.png" width = "500" alt="擦除flash" align=center />
</div>

## 3. Website of Firmware
在这里将归纳一些与K210固件相关的网站。

- 烧写固件教程网站为：
- 固件下载站为：https://api.dl.sipeed.com/shareURL/MAIX/MaixPy/release/master。