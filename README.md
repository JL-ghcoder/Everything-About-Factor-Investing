# Everything-About-Factor-Investing

## 概览

本项目旨在尽可能全面的展示有关因子投资的理论与实践方法

## 目录

[第一章 因子投资基础]([1]因子投资基础.md)


[第二章 因子投资方法论]([2]因子投资方法论.md)

## 数据与回测

数据主要来源于rqdatac，也可以替换成tushare等类似的第三方数据源。

回测引擎 - [Athena](https://github.com/JL-ghcoder/Athena)

Athena是我自研的一个简单的事件型回测框架，详情可见这个[仓库](https://github.com/JL-ghcoder/Athena)，通过重写框架我们可以尽可能的从底层实现与因子研究相关的方法。

值得一提的是我并没有去使用alphalens这样的工具，因为我想更接近因子研究的本质，前者的框架应该是基于向量化的速度一定会比我自己实现的事件驱动框架快很多。但是从一个最简框架一步步定制，你会发现一些有意思的东西，这是用第三方工具无法感受到的。

## 参考资料

因子投资-方法与实践 -- 石川; 刘洋溢; 连祥斌 -- 2020 -- 电子工业出版社
