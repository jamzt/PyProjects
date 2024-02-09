from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction 

# this function will render the Home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None) #retrive transaction form
    #checks if request method is POST
    if request.method == 'POST':
        pk = request.POST['account'] #if the form is submitted,retrive which account the user wants to view
        return balance(request, pk) #call balance function to render that acc's Balance Sheet
    content = {'form': form} #saves content to the template as a dictionary
    #adds content of form to page
    return render(request, 'checkbook/index.html', content)


#this function will render the Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None) #retrieves the Account form
    #checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): #check to see if the submitted form is valid and if som saves the form 
            form.save() #saves new acc
            return redirect('index') #returns user back to the home page
    content = {'form': form} #saves content to the template as a dictionary
    #adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


#this function will render the Balance page when requested 
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) #retrieve the requested acc isong its primary key
    transactions = Transaction.Transactions.filter(account=pk) #retrive all of that acc's transactions
    current_total =account.initial_deposit #create acc variable, starting with initial deposit value
    table_contents = {} #create a dictionary into which transaction info will be placed
    for t in transactions: #loop through transactions and determine which is a deposit or withdrawal
        if t.type == 'Deposit':
            current_total += t.amount #if deposit add amount to balance 
            table_contents.update({t: current_total}) #add transaction and total to the dictionary
        else:
            current_total -= t.amount #if withdrawal substract amount from balance 
            table_contents.update({t: current_total}) #add transaction and total to the dictionary
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)



# this function will render the Transactiom pahe when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None) #retrieves the Transaction form
    #checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): #check to see if the submitted form is valid and if som saves the form 
            pk = request.POST['account'] #retrieve which acc the transaction was for
            form.save() #saves new acc
            return balance(request, pk) #renders BS of the accounts BS
    #pass content to the template in a dictionary
    content = {'form': form} 
    #adds content of form to page
    return render(request, 'checkbook/AddTransaction.html', content)
