# Calories Burnt Prediction

This project aims to predict the number of calories burned by a user based on several features like gender, age, height, weight, duration of the exercise, heart rate, and body temperature. The dataset consists of user information and their corresponding calories burned after exercise.

## Dataset

The dataset contains the following features:

- **User_ID**: Unique identifier for each user
- **Gender**: Gender of the user (Male/Female)
- **Age**: Age of the user
- **Height**: Height of the user (in cm)
- **Weight**: Weight of the user (in kg)
- **Duration**: Duration of exercise in minutes
- **Heart_Rate**: Heart rate during exercise (beats per minute)
- **Body_Temp**: Body temperature during exercise (in Celsius)
- **Calories**: Target variable representing calories burnt (in kcal)

### Sample Data:

| User_ID   | Gender | Age | Height | Weight | Duration | Heart_Rate | Body_Temp | Calories |
|-----------|--------|-----|--------|--------|----------|------------|-----------|----------|
| 10001159  | female | 67  | 176.0  | 74.0   | 12.0     | 103.0      | 39.6      | 76.0     |
| 10001607  | female | 34  | 178.0  | 79.0   | 19.0     | 96.0       | 40.6      | 93.0     |
| 10005485  | female | 38  | 178.0  | 77.0   | 14.0     | 82.0       | 40.5      | 49.0     |
| 10005630  | female | 39  | 169.0  | 66.0   | 8.0      | 90.0       | 39.6      | 36.0     |
| 10006441  | male   | 23  | 169.0  | 73.0   | 25.0     | 102.0      | 40.7      | 122.0    |

## Libraries Used

- **pandas**: For data manipulation and preprocessing
- **matplotlib**: For data visualization
- **scikit-learn**: For building and evaluating machine learning models
- **numpy**: For numerical operations
- **seaborn**: For advanced data visualization

## Models Used

1. **Linear Regression**
2. **KNN (K-Nearest Neighbors)**
3. **Decision Tree**
4. **Random Forest**
5. **AdaBoost**
   
## Best Model

The **Random Forest** model performed the best with a prediction accuracy of **99%** on the test data.

## Model Evaluation

The performance of the models was evaluated using metrics like Mean Squared Error (MSE) and R-squared value. The Random Forest model demonstrated the highest accuracy, making it the optimal choice for this prediction task.


## Conclusion

This project demonstrates the use of various machine learning algorithms for predicting calories burned based on user attributes. The Random Forest model has proven to be highly accurate, making it suitable for real-time predictions.

