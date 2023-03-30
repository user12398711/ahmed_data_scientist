# Practical 1
x = c(8, 8, 9, 9, 9, 11, 12, 13, 13, 14, 15)
t.test(x, mu=10, conf.level=0.95, alternative="less")
# Practical 2
x = c(8, 8, 9, 9, 9, 11, 12, 13, 13, 14, 15)
y = c(11, 12, 13, 14, 14, 14, 15, 16, 18, 18, 19)
t.test(x, y, conf.level=0.95)
# Practical 3
x = c(8, 8, 9, 9, 9, 11, 12, 13, 13, 14, 15)
y = c(11, 12, 13, 14, 14, 14, 15, 16, 18, 18, 19)
t.test(x, y, conf.level=0.95, paired=TRUE)
# Practical 4
summary(aov(mtcars$disp ~ factor(mtcars$gear)))
# Practical 5
summary(aov(mtcars$disp ~ factor(mtcars$gear) * factor(mtcars$gear)))
# Practical 6
x = c(151, 174, 138, 186, 128, 136, 170, 163, 152, 131)
y = c(63, 81, 56, 91, 47, 57, 72, 62, 48, 56)
rel_xy = lm(y~x)
print(rel_xy)
a = data.frame(x=170)
res = predict(rel_xy, a)
print(res)
# Practical 7
x = c(38.9, 61.2, 73.3, 21.8, 63.4, 64.6, 48.4, 48.8)
y = c(47.8, 60, 63.4, 76, 89.4, 67.3, 31.3, 62.4)
A = c(x, y)
B = rep(c("x", "y"), each=8)
DATA = data.frame(x, y, StringAsFactors = TRUE)
wilcox.test(A~B, data=DATA, exact=FALSE)
# Practical 8
score = c(75,77,83,78,83,89,90,91,97,77,80,84,84,85,90,92,94,95,96,87)
method = rep(c("M1", "M2"), each=10)
DATA = data.frame(method, score, StringasFactors=TRUE)
library(coin)
median_test(method~score, data=DATA)
# Practical 9
height = c(7,14,14,13,12,9,6,14,12,8,15,17,13,15,15,15,9,12,10,8,6,8,8,9,5,14,13,8,10,9)
df = data.frame(group = rep(c("A", "B", "C"), each=10))
kruskal.test(height~group, data=df)
