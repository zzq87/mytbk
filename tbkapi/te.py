import top.api
import json
# 获取淘宝客商品优惠券

def get_tbk_coupon( page, keyword):
    req = top.api.TbkDgItemCouponGetRequest()
    req.set_app_info(top.appinfo('23464946', '9f11bf3465371f7bea54c7941e53b40a'))

    req.adzone_id = '61894823'
    # 商品的平台：1为PC端，2为无线端，默认为1
    req.platform = 2
    # 商品的类目ID
    #req.cat = "16,18"
    # 每页返回的商品数量
    req.page_size = 40
    # 商品的搜索词
    req.q = keyword
    # 返回商品的页数
    req.page_no = page
    try:
        resp = req.getResponse()
        s = resp['tbk_dg_item_coupon_get_response']['results']['tbk_coupon']
        for i in s:
            print(i['item_url'], i['title'], i['volume'], i['zk_final_price'], i['coupon_info'], i['commission_rate'], i['coupon_click_url'])
        print(resp['tbk_dg_item_coupon_get_response']['total_results'])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    for i in range(1, 5):
        print(i)
        get_tbk_coupon(i, '九阳电饭煲')