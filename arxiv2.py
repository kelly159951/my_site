import requests
from lxml import etree
import json
def request_pdf(start_url,request_urls, headers):
    response = requests.get(start_url, headers=headers)
    response.encoding = 'utf-8'
    tree = etree.HTML(response.text)
    response_urls = tree.xpath('//div[@class="content"]/ol[@class="breathe-horizontal"]/li[@class="arxiv-result"]/div/p/span/a/@href')
    # urls.extend([[html.split('..')[-1] for html in response_urls]])
    flag = False
    tmp = []
    for html in response_urls:
        flag = not flag
        if flag:
            tmp.append(html.split('..')[-1])
    request_urls = tmp
    return request_urls

def request_label(start_url,request_urls,headers):
    response = requests.get(start_url, headers=headers)
    response.encoding = 'utf-8'
    tree = etree.HTML(response.text)
    response_urls = tree.xpath('//div[@class="content"]/ol[@class="breathe-horizontal"]/li[@class="arxiv-result"]/div/p/a//text()')
    # for html in response_urls:
    #     dict[html] = {}
    #label_urls.extend([[html for html in response_urls]])
    #return label_urls
    request_urls = response_urls
    return request_urls

def request_submit_announce(start_url,headers):
    response = requests.get(start_url, headers=headers)
    response.encoding = 'utf-8'
    tree = etree.HTML(response.text)
    response_urls = []
    list1 = []
    list2 = []
    for i in range(50):
        response_urls = tree.xpath('//div[@class="content"]/ol[@class="breathe-horizontal"]/li[{}]/p[@class="is-size-7"]//text()'.format(i+1))
        tmp = response_urls[1].split('; \n      ')
        response_urls[1] = ''.join(tmp)
        tmp = response_urls[3].split('\n      \n    ')
        response_urls[3] = ''.join(tmp)
        list1.append(response_urls[1])
        list2.append(response_urls[3])
    # for html in response_urls:
    #     dict[html] = {}
    #label_urls.extend([[html for html in response_urls]])
    #return label_urls
    return list1,list2

def request_name(start_url, request_urls, headers):
    response = requests.get(start_url, headers=headers)
    response.encoding = 'utf-8'
    tree = etree.HTML(response.text)
    for i in range(50):
        response_urls = tree.xpath('//div[@class="content"]/ol[@class="breathe-horizontal"]/li[{}]/p[@class = "title is-5 mathjax"]//text()'.format(i+1))
        list1 = [str(html) for html in response_urls]
        str4 = ''.join(list1)
        list2 = str4.split('\n      \n    ')
        str5 =(''.join(list2)).strip()
        request_urls.append(str5)

    #name_urls.extend([[html for html in response_urls]])
    return request_urls

def request_author(start_url, request_urls, headers):
    response = requests.get(start_url, headers=headers)
    response.encoding = 'utf-8'
    tree = etree.HTML(response.text)
    for i in range(50):
        response_urls = tree.xpath('//div[@class="content"]/ol[@class="breathe-horizontal"]/li[{}]/p[@class = "authors"]/a//text()'.format(i+1))
        # author_urls.extend([[html for html in response_urls]])
        request_urls.append(response_urls)

    #response_urls = tree.xpath('//div[@class="content"]/ol[@class="breathe-horizontal"]/li[@class="arxiv-result"]/p[@class = "authors"]/a//text()')
    # urls.extend([[html.split('..')[-1] for html in response_urls]])

    #author_urls.extend([[html for html in response_urls]])
    return request_urls


def request_abstract_short(start_url, request_urls, headers):
    response = requests.get(start_url, headers=headers)
    response.encoding = 'utf-8'
    tree = etree.HTML(response.text)
    for i in range(50):
        response_urls_1 = tree.xpath('//div[@class="content"]/ol[@class="breathe-horizontal"]/li[{}]/p[@class = "abstract mathjax"]/span[@class="abstract-short has-text-grey-dark mathjax"]//text()'.format(i+1))
        # response_urls_2 = tree.xpath('//div[@class="content"]/ol[@class="breathe-horizontal"]/li[{}]/p[@class = "abstract mathjax"]/span[@class="abstract-full has-text-grey-dark mathjax"]//text()'.format(i+1))
        list1 = [str(html) for html in response_urls_1]
        str4 = ''.join(list1)
        list2 = str4.split('\n        ')
        str5 =(''.join(list2)).strip()
        list3 =str5.split('…▽ More')
        str6 = ''.join(list3)
        # list1 = [str(html) for html in response_urls_2]
        # str4 = ''.join(list1)
        # list2 = str4.split('\n        ')
        # str5 =(''.join(list2)).strip()
        # list3 =str5.split('△ Less')
        # str7 = ''.join(list3)
        request_urls.append(str6)
    #response_urls = tree.xpath('//div[@class="content"]/ol[@class="breathe-horizontal"]/li[@class="arxiv-result"]/p[@class = "authors"]/a//text()')
    # urls.extend([[html.split('..')[-1] for html in response_urls]])

    #author_urls.extend([[html for html in response_urls]])
    return request_urls



def request_abstract(start_url, request_urls, headers):
    response = requests.get(start_url, headers=headers)
    response.encoding = 'utf-8'
    tree = etree.HTML(response.text)
    for i in range(50):
        response_urls_1 = tree.xpath('//div[@class="content"]/ol[@class="breathe-horizontal"]/li[{}]/p[@class = "abstract mathjax"]/span[@class="abstract-short has-text-grey-dark mathjax"]//text()'.format(i+1))
        response_urls_2 = tree.xpath('//div[@class="content"]/ol[@class="breathe-horizontal"]/li[{}]/p[@class = "abstract mathjax"]/span[@class="abstract-full has-text-grey-dark mathjax"]//text()'.format(i+1))
        list1 = [str(html) for html in response_urls_1]
        str4 = ''.join(list1)
        list2 = str4.split('\n        ')
        str5 =(''.join(list2)).strip()
        list3 =str5.split('…▽ More')
        str6 = ''.join(list3)
        list1 = [str(html) for html in response_urls_2]
        str4 = ''.join(list1)
        list2 = str4.split('\n        ')
        str5 =(''.join(list2)).strip()
        list3 =str5.split('△ Less')
        str7 = ''.join(list3)
        request_urls.append(str6+str7)
    #response_urls = tree.xpath('//div[@class="content"]/ol[@class="breathe-horizontal"]/li[@class="arxiv-result"]/p[@class = "authors"]/a//text()')
    # urls.extend([[html.split('..')[-1] for html in response_urls]])

    #author_urls.extend([[html for html in response_urls]])
    return request_urls

start_url = "https://arxiv.org/search/cs?query=machine+learning&searchtype=all&abstracts=show&order=-announced_date_first&size=50"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64\
           ) AppleWebKit/537.36 (KHTML, like Gecko) \
           Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76'}
# response = requests.get("https://arxiv.org/search/cs?query=neural+network&searchtype=all&abstracts=show&order=-announced_date_first&size=50")
# print(response)
dict1 = {}

lst = []
# list_name = request_name(start_url,[], headers)
# print(list_name)
list_name = ['Idempotent Generative Network', 'Implicit Chain of Thought Reasoning via Knowledge Distillation', 'Detecting Deepfakes Without Seeing Any', 'RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation', 'PPI++: Efficient Prediction-Powered Inference', 'Time Series Anomaly Detection using Diffusion-based Models', 'DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing', 'UltraLiDAR: Learning Compact Representations for LiDAR Completion and Generation', 'CADSim: Robust and Scalable in-the-wild 3D Reconstruction for Controllable Sensor Simulation', 'Adv3D: Generating Safety-Critical 3D Objects through Closed-Loop Simulation', 'Deep Double Descent for Time Series Forecasting: Avoiding Undertrained Models', 'Distilling Out-of-Distribution Robustness from Vision-Language Foundation Models', 'Contrastive Moments: Unsupervised Halfspace Learning in Polynomial Time', 'Tailoring Mixup to Data using Kernel Warping functions', 'Identifying Alzheimer Disease Dementia Levels Using Machine Learning Methods', 'Exploring Deep Learning Techniques for Glaucoma Detection: A Comprehensive Review', 'Holistic Transfer: Towards Non-Disruptive Fine-Tuning with Partial Target Data', 'Castor: Causal Temporal Regime Structure Learning', 'The Blessing of Randomness: SDE Beats ODE in General Diffusion-based Image Editing', 'A Coreset-based, Tempered Variational Posterior for Accurate and Scalable Stochastic Gaussian Process Inference', 'Analysis of Information Propagation in Ethereum Network Using Combined Graph Attention Network and Reinforcement Learning to Optimize Network Efficiency and Scalability', 'Learning to See Physical Properties with Active Sensing Motor Policies', 'Normalizing flows as approximations of optimal transport maps via linear-control neural ODEs', 'Learning Realistic Traffic Agents in Closed-loop', 'Time-series Generation by Contrastive Imitation', 'Vision-Language Foundation Models as Effective Robot Imitators', 'Monotone Generative Modeling via a Gromov-Monge Embedding', 'Respiratory Anomaly Detection using Reflected Infrared Light-wave Signals', 'On the Lipschitz constant of random neural networks', 'Deep learning based Image Compression for Microscopy Images: An Empirical Study', 'Unreading Race: Purging Protected Features from Chest X-ray Embeddings', 'Like an Open Book? Read Neural Network Architecture with Simple Power Analysis on 32-bit Microcontrollers', 'Offline Imitation from Observation via Primal Wasserstein State Occupancy Matching', 'A Simple Solution for Offline Imitation from Observations and Examples with Possibly Incomplete Trajectories', 'High-dimensional Linear Bandits with Knapsacks', 'Towards Evaluating Transfer-based Attacks Systematically, Practically, and Fairly', 'Scattering Vision Transformer: Spectral Mixing Matters', 'AWEQ: Post-Training Quantization with Activation-Weight Equalization for Large Language Models', 'TRIALSCOPE A Unifying Causal Framework for Scaling Real-World Evidence Generation with Biomedical Language Models', 'DP-Mix: Mixup-based Data Augmentation for Differentially Private Learning', 'FlashDecoding++: Faster Large Language Model Inference on GPUs', 'Long-Range Neural Atom Learning for Molecular Graphs', 'An energy-based comparative analysis of common approaches to text classification in the Legal domain', 'Human participants in AI research: Ethics and transparency in practice', 'Sanitized Clustering against Confounding Bias', 'Push it to the Demonstrated Limit: Multimodal Visuotactile Imitation Learning with Force Matching', 'Multi-Operational Mathematical Derivations in Latent Space', 'Diffusion Models for Reinforcement Learning: A Survey', 'Attacking Graph Neural Networks with Bit Flips: Weisfeiler and Lehman Go Indifferent', 'Federated Learning on Edge Sensing Devices: A Review']

# print(list_abstract)
# list_abstract = 
# list_author = request_author(start_url,[],headers)
# print(list_author)
list_author=[['Assaf Shocher', 'Amil Dravid', 'Yossi Gandelsman', 'Inbar Mosseri', 'Michael Rubinstein', 'Alexei A. Efros'], ['Yuntian Deng', 'Kiran Prasad', 'Roland Fernandez', 'Paul Smolensky', 'Vishrav Chaudhary', 'Stuart Shieber'], ['Tal Reiss', 'Bar Cavia', 'Yedid Hoshen'], ['Yufei Wang', 'Zhou Xian', 'Feng Chen', 'Tsun-Hsuan Wang', 'Yian Wang', 'Katerina Fragkiadaki', 'Zackory Erickson', 'David Held', 'Chuang Gan'], ['Anastasios N. Angelopoulos', 'John C. Duchi', 'Tijana Zrnic'], ['Ioana Pintilie', 'Andrei Manolache', 'Florin Brad'], ['Vint Lee', 'Pieter Abbeel', 'Youngwoon Lee'], ['Yuwen Xiong', 'Wei-Chiu Ma', 'Jingkang Wang', 'Raquel Urtasun'], ['Jingkang Wang', 'Sivabalan Manivasagam', 'Yun Chen', 'Ze Yang', 'Ioan Andrei Bârsan', 'Anqi Joyce Yang', 'Wei-Chiu Ma', 'Raquel Urtasun'], ['Jay Sarva', 'Jingkang Wang', 'James Tu', 'Yuwen Xiong', 'Sivabalan Manivasagam', 'Raquel Urtasun'], ['Valentino Assandri', 'Sam Heshmati', 'Burhaneddin Yaman', 'Anton Iakovlev', 'Ariel Emiliano Repetur'], ['Andy Zhou', 'Jindong Wang', 'Yu-Xiong Wang', 'Haohan Wang'], ['Xinyuan Cao', 'Santosh S. Vempala'], ['Quentin Bouniot', 'Pavlo Mozharovskyi', "Florence d'Alché-Buc"], ['Md Gulzar Hussain', 'Ye Shiren'], ['Aized Amin Soofi', ' Fazal-e-Amin'], ['Cheng-Hao Tu', 'Hong-You Chen', 'Zheda Mai', 'Jike Zhong', 'Vardaan Pahuja', 'Tanya Berger-Wolf', 'Song Gao', 'Charles Stewart', 'Yu Su', 'Wei-Lun Chao'], ['Abdellah Rahmani', 'Pascal Frossard'], ['Shen Nie', 'Hanzhong Allan Guo', 'Cheng Lu', 'Yuhao Zhou', 'Chenyu Zheng', 'Chongxuan Li'], ['Mert Ketenci', 'Adler Perotte', 'Noémie Elhadad', 'Iñigo Urteaga'], ['Stefan Kambiz Behfar', 'Jon Crowcroft'], ['Gabriel B. Margolis', 'Xiang Fu', 'Yandong Ji', 'Pulkit Agrawal'], ['Alessandro Scagliotti', 'Sara Farinelli'], ['Chris Zhang', 'James Tu', 'Lunjun Zhang', 'Kelvin Wong', 'Simon Suo', 'Raquel Urtasun'], ['Daniel Jarrett', 'Ioana Bica', 'Mihaela van der Schaar'], ['Xinghang Li', 'Minghuan Liu', 'Hanbo Zhang', 'Cunjun Yu', 'Jie Xu', 'Hongtao Wu', 'Chilam Cheang', 'Ya Jing', 'Weinan Zhang', 'Huaping Liu', 'Hang Li', 'Tao Kong'], ['Wonjun Lee', 'Yifei Yang', 'Dongmian Zou', 'Gilad Lerman'], ['Md Zobaer Islam', 'Brenden Martin', 'Carly Gotcher', 'Tyler Martinez', "John F. O'Hara", 'Sabit Ekin'], ['Paul Geuchen', 'Thomas Heindl', 'Dominik Stöger', 'Felix Voigtlaender'], ['Yu Zhou', 'Jan Sollman', 'Jianxu Chen'], ['Tobias Weber', 'Michael Ingrisch', 'Bernd Bischl', 'David Rügamer'], ['Raphael Joud', 'Pierre-Alain Moellic', 'Simon Pontie', 'Jean-Baptiste Rigaud'], ['Kai Yan', 'Alexander G. Schwing', 'Yu-xiong Wang'], ['Kai Yan', 'Alexander G. Schwing', 'Yu-Xiong Wang'], ['Wanteng Ma', 'Dong Xia', 'Jiashuo Jiang'], ['Qizhang Li', 'Yiwen Guo', 'Wangmeng Zuo', 'Hao Chen'], ['Badri N. Patro', 'Vijay Srinivas Agneeswaran'], ['Baisong Li', 'Xingwang Wang', 'Haixiao Xu'], ['Javier González', 'Cliff Wong', 'Zelalem Gero', 'Jass Bagga', 'Risa Ueno', 'Isabel Chien', 'Eduard Orakvin', 'Emre Kiciman', 'Aditya Nori', 'Roshanthi Weerasinghe', 'Rom S. Leidner', 'Brian Piening', 'Tristan Naumann', 'Carlo Bifulco', 'Hoifung Poon'], ['Wenxuan Bao', 'Francesco Pittaluga', 'Vijay Kumar B G', 'Vincent Bindschaedler'], ['Ke Hong', 'Guohao Dai', 'Jiaming Xu', 'Qiuli Mao', 'Xiuhong Li', 'Jun Liu', 'Kangdi Chen', 'Hanyu Dong', 'Yu Wang'], ['Xuan Li', 'Zhanke Zhou', 'Jiangchao Yao', 'Yu Rong', 'Lu Zhang', 'Bo Han'], ['Sinan Gultekin', 'Achille Globo', 'Andrea Zugarini', 'Marco Ernandes', 'Leonardo Rigutini'], ['Kevin R. McKee'], ['Yinghua Yao', 'Yuangang Pan', 'Jing Li', 'Ivor W. Tsang', 'Xin Yao'], ['Trevor Ablett', 'Oliver Limoyo', 'Adam Sigal', 'Affan Jilani', 'Jonathan Kelly', 'Kaleem Siddiqi', 'Francois Hogan', 'Gregory Dudek'], ['Marco Valentino', 'Jordan Meadows', 'Lan Zhang', 'André Freitas'], ['Zhengbang Zhu', 'Hanye Zhao', 'Haoran He', 'Yichao Zhong', 'Shenyu Zhang', 'Yong Yu', 'Weinan Zhang'], ['Lorenz Kummer', 'Samir Moustafa', 'Nils N. Kriege', 'Wilfried N. Gansterer'], ['Berrenur Saylam', 'Özlem Durmaz İncel']]
# list_label = request_label(start_url,[],headers)
# print(list_label)
list_label = ['arXiv:2311.01462', 'arXiv:2311.01460', 'arXiv:2311.01458', 'arXiv:2311.01455', 'arXiv:2311.01453', 'arXiv:2311.01452', 'arXiv:2311.01450', 'arXiv:2311.01448', 'arXiv:2311.01447', 'arXiv:2311.01446', 'arXiv:2311.01442', 'arXiv:2311.01441', 'arXiv:2311.01435', 'arXiv:2311.01434', 'arXiv:2311.01428', 'arXiv:2311.01425', 'arXiv:2311.01420', 'arXiv:2311.01412', 'arXiv:2311.01410', 'arXiv:2311.01409', 'arXiv:2311.01406', 'arXiv:2311.01405', 'arXiv:2311.01404', 'arXiv:2311.01394', 'arXiv:2311.01388', 'arXiv:2311.01378', 'arXiv:2311.01375', 'arXiv:2311.01367', 'arXiv:2311.01356', 'arXiv:2311.01352', 'arXiv:2311.01349', 'arXiv:2311.01344', 'arXiv:2311.01331', 'arXiv:2311.01329', 'arXiv:2311.01327', 'arXiv:2311.01323', 'arXiv:2311.01310', 'arXiv:2311.01305', 'arXiv:2311.01301', 'arXiv:2311.01295', 'arXiv:2311.01282', 'arXiv:2311.01276', 'arXiv:2311.01256', 'arXiv:2311.01254', 'arXiv:2311.01252', 'arXiv:2311.01248', 'arXiv:2311.01230', 'arXiv:2311.01223', 'arXiv:2311.01205', 'arXiv:2311.01201']
# list_pdf = request_pdf(start_url,[],headers)
# print(list_pdf)


list_pdf = ['https://arxiv.org/pdf/2311.01462', 'https://arxiv.org/pdf/2311.01460', 'https://arxiv.org/pdf/2311.01458', 'https://arxiv.org/pdf/2311.01455', 'https://arxiv.org/pdf/2311.01453', 'https://arxiv.org/pdf/2311.01452', 'https://arxiv.org/pdf/2311.01450', 'https://arxiv.org/pdf/2311.01448', 'https://arxiv.org/pdf/2311.01447', 'https://arxiv.org/pdf/2311.01446', 'https://arxiv.org/pdf/2311.01442', 'https://arxiv.org/pdf/2311.01441', 'https://arxiv.org/pdf/2311.01435', 'https://arxiv.org/pdf/2311.01434', 'https://arxiv.org/pdf/2311.01428', 'https://arxiv.org/pdf/2311.01425', 'https://arxiv.org/pdf/2311.01420', 'https://arxiv.org/pdf/2311.01412', 'https://arxiv.org/pdf/2311.01410', 'https://arxiv.org/pdf/2311.01409', 'https://arxiv.org/pdf/2311.01406', 'https://arxiv.org/pdf/2311.01405', 'https://arxiv.org/pdf/2311.01404', 'https://arxiv.org/pdf/2311.01394', 'https://arxiv.org/pdf/2311.01388', 'https://arxiv.org/pdf/2311.01378', 'https://arxiv.org/pdf/2311.01375', 'https://arxiv.org/pdf/2311.01367', 'https://arxiv.org/pdf/2311.01356', 'https://arxiv.org/pdf/2311.01352', 'https://arxiv.org/pdf/2311.01349', 'https://arxiv.org/pdf/2311.01344', 'https://arxiv.org/pdf/2311.01331', 'https://arxiv.org/pdf/2311.01329', 'https://arxiv.org/pdf/2311.01327', 'https://arxiv.org/pdf/2311.01323', 'https://arxiv.org/pdf/2311.01310', 'https://arxiv.org/pdf/2311.01305', 'https://arxiv.org/pdf/2311.01301', 'https://arxiv.org/pdf/2311.01295', 'https://arxiv.org/pdf/2311.01282', 'https://arxiv.org/pdf/2311.01276', 'https://arxiv.org/pdf/2311.01256', 'https://arxiv.org/pdf/2311.01254', 'https://arxiv.org/pdf/2311.01252', 'https://arxiv.org/pdf/2311.01248', 'https://arxiv.org/pdf/2311.01230', 'https://arxiv.org/pdf/2311.01223', 'https://arxiv.org/pdf/2311.01205', 'https://arxiv.org/pdf/2311.01201']
# print(len(list_pdf))
#list_abstract = request_abstract_short(start_url,[],headers)
list_submit,list_announce = request_submit_announce(start_url,headers)


for i in range(50):
    print(i)
    dict1[list_label[i]] = {}
    dict1[list_label[i]]["name"] = list_name[i]
    dict1[list_label[i]]["author"] = list_author[i]
    #dict1[list_label[i]]["abstract"] = list_abstract[i]
    dict1[list_label[i]]["pdf"] = list_pdf[i]
    dict1[list_label[i]]["submitted time"] = list_submit[i]
    dict1[list_label[i]]["announced time"] = list_announce[i]
    print(i)

json_str = json.dumps(dict1)
print(json_str)
with open('arxiv.json', 'w',encoding='utf-8') as json_file:
    json_file.write(json_str)
    print(22222)