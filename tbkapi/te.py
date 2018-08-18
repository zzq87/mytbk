import top.api
import re

# 获取淘宝客商品优惠券

def get_tbk_coupon( page, keyword, xl, yj): #好券清单
    req = top.api.TbkDgItemCouponGetRequest()
    req.set_app_info(top.appinfo('23464946', '9f11bf3465371f7bea54c7941e53b40a'))

    req.adzone_id = '61894823'
    req.page_size = 50 # 每页数量
    req.q = keyword # 搜索关键词
    req.page_no = page #页码
    xl = xl #月销量
    yj = yj #佣金率

    try:
        resp = req.getResponse()
        s = resp['tbk_dg_item_coupon_get_response']['results']['tbk_coupon']
        for i in s:
            if int(i['volume']) >= xl:
                if float(i['commission_rate']) >= yj:
                    y = re.findall(r'\d+', i['coupon_info'])
                    qhj = round(float(i['zk_final_price'])-float(y[1]), 2)
                    print(i['item_url'], i['title'], i['volume'], i['zk_final_price'], i['coupon_info'], \
                          '券后价'+str(qhj), '佣金'+i['commission_rate'], i['coupon_click_url'])
                    #     商品链接       商品标题    月销量       折扣价格             优惠券信息        \
                    #  券后价            佣金                          优惠券链接
    except Exception as e:
        print(e)


if __name__ == '__main__':
    for i in range(1, 3):
        print(i)
        get_tbk_coupon(i, '自喷漆', 50, 1)
