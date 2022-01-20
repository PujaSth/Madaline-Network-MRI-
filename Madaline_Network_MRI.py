#taking the input from user
input_value=[]
target_value=[]
pattern_number=eval(input('Enter the total number of pattern: '))
number_of_input_for_each_pattern=[]
for i in range(pattern_number):
    print('\nEnter the total number of inputs for pattern',i+1)
    number_of_input=eval(input())
    number_of_input_for_each_pattern.append(number_of_input)
    tmp=[]
    for j in range(number_of_input_for_each_pattern[i]):
        print('enter the input x',j+1,'for pattern',i+1)
        x=eval(input())
        tmp.append(x)
    input_value.append(tmp)    
    print('Enter the target for pattern',i+1,':')
    target=eval(input())
    target_value.append(target)

#inputs from hidden layer
node_bias_list=[]
hidden_layer_number=eval(input('Enter the number of hidden layer : '))
node_weight=[]

hidden_node_number_list=[number_of_input_for_each_pattern[0]]
for i in range (hidden_layer_number):
    node_bias=[]
    print('Enter the number of nodes in ',i+1,' hidden layer : ')
    hidden_node_number=eval(input())
    hidden_node_number_list.append(hidden_node_number)
    for j in range(hidden_node_number):
        temp=[]
        print('\nEnter the weight for node',j+1,'of ',i+1,'layer:')
        for k in range (hidden_node_number_list[i]):
            hidden_value= eval(input())
            temp.append(hidden_value)
        node_weight.append(temp)
        print('\nEnter the bias for node',j+1,'of ',i+1,'layer:')
        bias = eval(input())
        node_bias.append(bias)
    node_bias_list.append(node_bias)

#taking the weights of all nodes in output layer
tmp=[]
output_node_weight=[]
print('\nEnter the weight for node of output layer:')
for j in range(hidden_node_number_list[len(hidden_node_number_list)-1]):
   output_wt=eval(input())
   tmp.append(output_wt)
output_node_weight.append(tmp)
print('Initial weight is: ',node_weight,'\nInitial bias is: ',node_bias_list) 
    
#Initialize weight and bias
learning_rate=0.5
output_node_bias=0.5

#calculations
old_weight=node_weight[:]
old_bias=node_bias_list[:]

Zin_list=[]
for i in range(pattern_number):
    Zin=[]
    new_weight=[]
    new_bias_list=[]
    new_bias=[]
    for j in range(hidden_layer_number):
        for l in range(number_of_input_for_each_pattern[j]):
            a=0
            for k in range(hidden_node_number_list[j+1]):
                a += input_value[i][k] * old_weight[l][k]
            Zin_value= old_bias[j][l]+a
            Zin.append(Zin_value)
        Zin_list.append(Zin)
        if(Zin_list[i][j] >= 0):
            z1 = 1
        else:
            z1 = -1
        if(Zin_list[i][j+1] >= 0):
            z2 = 1 
        else:
            z2 = -1
        yin = output_node_bias + z1*output_node_weight[0][j] + z2*output_node_weight[0][j+1]
        
        if(yin>=0):
            y=1
        else:
            y=-1
        target=target_value[i]
        if((y!=target) and (target==-1)):
            for m in range(hidden_node_number_list[j+1]):
                weight=[]
                for n in range(hidden_node_number_list[j]):
                    wt = old_weight[m][n] + learning_rate * (-1-Zin_list[i][m])*input_value[i][n]
                    weight.append(wt)
                new_weight.append(weight)
                bias_value=old_bias[j][m] + learning_rate*(-1-Zin_list[i][m])
                new_bias.append(bias_value)
            new_bias_list.append(new_bias)
            old_weight=new_weight
            old_bias=new_bias_list
            #print('weight :',old_weight)
            #print('bias :',old_bias)
        elif((y!=target) and (target==1)):
             for m in range(hidden_node_number_list[j+1]):
                weight=[]
                for n in range(hidden_node_number_list[j]):
                    wt = old_weight[m][n] + learning_rate * (1-Zin_list[i][m])*input_value[i][n]
                    weight.append(wt)
                new_weight.append(weight)
                bias_value=old_bias[j][m] + learning_rate*(1-Zin_list[i][m])
                new_bias.append(bias_value)
             new_bias_list.append(new_bias)
             old_weight=new_weight
             old_bias=new_bias_list
             #print('weight :',old_weight)
             #print('bias :',old_bias)
        else:
            old_weight=old_weight
            old_bias= old_bias
         
#display 
print('Number of input for each pattern: ',number_of_input_for_each_pattern)
print('Value of input for each pattern: ',input_value)
print('Target value: ',target_value)
print('Hidden node number list: ',hidden_node_number_list)
print('Weight Update :',old_weight)
print('Bias Update :',old_bias)

