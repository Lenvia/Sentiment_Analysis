from dict_classifier import DictClassifier

ds = DictClassifier()

# # 对一个单句进行情感分析
# a_sentence = "怀着十分激动的心情放映，可是看着看着发现，在放映完毕后，出现一集米老鼠的动画片！开始还怀疑是不是赠送的个别现象，可是后来发现每张DVD后面都有！真不知道生产商怎么想的，我想看的是猫和老鼠，不是米老鼠！如果厂家是想赠送的话，那就全套米老鼠和唐老鸭都赠送，只在每张DVD后面添加一集算什么？？简直是画蛇添足！！"
# # a_sentence = "这本书也许你不会一气读完，也许它不够多精彩，但确实是一本值得用心去看的书。活在当下，所谓的悲伤和恐惧都是人脑脱离当下自己瞎想出来的。书里的每句话每个理论都需要用心去体会，你会受益匪浅，这是真的！做个简单快乐的人，也不过如此。看了这本书，如果你用心去看了的话，会觉得豁然轻松了，一下子看开了，不会因为生活中的琐碎而成天担忧，惶恐不安。这是一本教你放下压力的值得一买的好书。"
# result = ds.analyse_sentence(a_sentence, print_show=False)
# print(result)


ds.evaluate("../../dataset/ChnSentiCorp/dev.tsv")