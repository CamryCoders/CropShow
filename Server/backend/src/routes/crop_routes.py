from flask import Blueprint
from src.controller.crop_recommend import cropRecommend
from src.middleware.validate_input import validate_input 
from src.controller.prob_chart import show_prediction_chart
from src.controller.Top3_recommend import top_3_crops
from src.controller.fertilizer_suggestion import fertilizer_suggestion

crop_routes =Blueprint(
    "crop_routes",
    __name__
)
crop_routes.route(
    "/crop_recommendation",
    methods=["GET"]
)(validate_input(cropRecommend))
# @validate_input
# def predict():
    
#     return cropRecommend()

crop_routes.route(
    "/prob_chart",
    methods=["GET"]
)(show_prediction_chart)

crop_routes.route(
    "/Top_3_crop",
    methods=["GET"]
)(top_3_crops)
crop_routes.route(
    "/fertilizer_suggestion",
    methods=["GET"]
)(fertilizer_suggestion)