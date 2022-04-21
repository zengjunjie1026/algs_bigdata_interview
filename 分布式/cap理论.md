CAP

C : consistency
A : available
P : partition 

分布式系统只能保证AP/CP


BASE理论

BA ： base available
基本可用

S soft status 软状态
E 最终一致性


RPC ： 远程过程调用
远程方法调用

RPC / http 有区别
http资源消耗更大
tcp也行

RPC over http
RPC over tcp


分布式ID是什么，有哪些解决方案？
分布式iD

1 uuid
2 单机自增主键，并发量大的时候扛不住
3 redis /zookeeper内置的命令生成id，性能略高
4 雪花算法，某一台机器在1ms内生成一个自增id，机器的id + time
能用算法解决的


分布式锁的应用场景？哪些实现方案？

zookeeper
redis


什么是分布式事物？有哪些实现方案？
1、本地消息表
2、消息队列


