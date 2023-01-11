import requests

url = "https://mamy-eyewear.com/wp-admin/admin-ajax.php"

payload = "atts%5Belement_title%5D=&atts%5Bpost_type%5D=product&atts%5Blayout%5D=grid&atts%5Binclude%5D=&atts%5Bcustom_query%5D=&atts%5Btaxonomies%5D=72&atts%5Bpagination%5D=more-btn&atts%5Bitems_per_page%5D=9&atts%5Bproduct_hover%5D=alt&atts%5Bspacing%5D=30&atts%5Bcolumns%5D=3&atts%5Bsale_countdown%5D=0&atts%5Bstock_progress_bar%5D=0&atts%5Bhighlighted_products%5D=0&atts%5Bproducts_bordered_grid%5D=0&atts%5Bproduct_quantity%5D=0&atts%5Boffset%5D=&atts%5Borderby%5D=modified&atts%5Bquery_type%5D=OR&atts%5Border%5D=&atts%5Bmeta_key%5D=&atts%5Bexclude%5D=&atts%5Bclass%5D=&atts%5Bajax_page%5D=&atts%5Bspeed%5D=5000&atts%5Bslides_per_view%5D=4&atts%5Bwrap%5D=&atts%5Bautoplay%5D=no&atts%5Bcenter_mode%5D=no&atts%5Bhide_pagination_control%5D=&atts%5Bhide_prev_next_buttons%5D=&atts%5Bscroll_per_page%5D=yes&atts%5Bcarousel_js_inline%5D=no&atts%5Bimg_size%5D=woocommerce_thumbnail&atts%5Bforce_not_ajax%5D=no&atts%5Bproducts_masonry%5D=&atts%5Bproducts_different_sizes%5D=&atts%5Blazy_loading%5D=no&atts%5Bscroll_carousel_init%5D=no&atts%5Bel_class%5D=&atts%5Bshop_tools%5D=no&paged=2&action=woodmart_get_products_shortcode&woo_ajax=1"
headers = {
  'authority': 'mamy-eyewear.com',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'cookie': '_fbp=fb.1.1673423881944.758851540; tk_or=%22https%3A%2F%2Fwww.google.com%2F%22; tk_r3d=%22https%3A%2F%2Fwww.google.com%2F%22; tk_lr=%22https%3A%2F%2Fwww.google.com%2F%22; _gid=GA1.2.201371525.1673423887; _gac_UA-216474929-1=1.1673423887.Cj0KCQiAtvSdBhD0ARIsAPf8oNkIa-vWmR0guKuEq7bPVEgnOQ75GXpnRKMu_nNJru52R8_SyBmJeIUaAlHwEALw_wcB; _gat_gtag_UA_216474929_1=1; _ga_R4080TX7WZ=GS1.1.1673423883.1.1.1673423891.0.0.0; _ga=GA1.2.1774934923.1673423884; woodmart_popup_1=shown',
  'origin': 'https://mamy-eyewear.com',
  'referer': 'https://mamy-eyewear.com/sunglasses/',
  'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)



