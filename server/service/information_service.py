from datetime import datetime

from repository import search_all_order_charges

def all_order_charges():
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    order_dic = search_all_order_charges(current_date)

    zero_vol_charge = f"{round(order_dic["row_result0"]["order_charge"]*100, 1)} %"
    
    over_vol = f"{str(order_dic["row_result1"]["min_volumn"])} Euro"
    
    over_vol_charge = f"{round(order_dic["row_result1"]["order_charge"]*100, 1)} %"
    
    print("order_dic", order_dic)

    information = {"line0": "Aktuelle Gebühren:",
                   "line1": f"bei einen Volumen von 0 Euro: {zero_vol_charge}",
                   "line2": f"ab einen Volumen von {over_vol}: {over_vol_charge}"}
    
    return information
    
if __name__ == "__main__":

    answer = all_order_charges()

    print(answer)

    for v in answer.values():
        print(v)