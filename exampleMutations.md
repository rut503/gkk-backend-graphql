mutation{
  createProducer(userInput: {
    firstName: "Rutvik",
    lastName: "Patel",
    phoneNumber: "48934",
    email: "Rutvik@patel.com",
    photo: "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1587&q=80",
    bio: "Something about me",
    address: {
      street: "984 Higgins Dr",
      city: "Hoffman",
      state: "IL",
      zipCode: "60294"
    }
  }){
    id
    firstName
    lastName
    phoneNumber
    email
    photo
    bio
    address {
      street
      city
      state
      zipCode
    }
    foodItemIds
    rating
    activeOrderIds
    dateCreated
    dateUpdated
  }
}

mutation{
  createConsumer(userInput: {
    firstName: "Rutvik",
    lastName: "Patel",
    phoneNumber: "48934",
    email: "Rutvik@patel.com",
    photo: "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1587&q=80",
    bio: "Something about me",
    address: {
      street: "984 Higgins Dr",
      city: "Hoffman",
      state: "IL",
      zipCode: "60294"
    }
  }){
    id
    firstName
    lastName
    phoneNumber
    email
    photo
    bio
    address {
      street
      city
      state
      zipCode
    }
    rating
    activeOrderIds
    dateCreated
    dateUpdated
  }
}

mutation{
  createFoodItem(foodItemInput: {
    producerId: "627b38840b85528df3ca06f4"
    dietPreferences: []
    description: "something about thepla"
    photo: "https://img-global.cpcdn.com/recipes/32f76a603871b445/1200x630cq70/photo.jpg"
    price: 3.99
    name: "Thepla"
    portionSize: 5
    spiciness: 1
    allergies: []
  }){
    id
    producerId
    dietPreferences
    description
    photo
    price
    rating
    name
    portionSize
    spiciness
    allergies
    dateCreated
    dateUpdated
  }
}

mutation{
  createReviewForProducer(userReviewInput: {
    producerId: "627b38840b85528df3ca06f7",
    consumerId: "627b38890b85528df3ca06fa",
    rating: 3,
    title: "Title of the review",
    description: "This is what review says."
  }){
    id
    producerId
    consumerId
    rating
    title
    description
    dateCreated
    dateUpdated
  }
}

mutation{
  createReviewForProducer(userReviewInput: {
    producerId: "627b38840b85528df3ca06f7",
    consumerId: "627b38890b85528df3ca06fa",
    rating: 3,
    title: "This is the title of the review",
    description: "This is what review says."
  }){
    id
    producerId
    consumerId
    rating
    title
    description
    dateCreated
    dateUpdated
  }
}

mutation{
  createReviewForFoodItem(foodItemReviewInput: {
    foodItemId: "627b38840b85528df3ca06f7",
    consumerId: "627b38890b85528df3ca06fa",
    rating: 3,
    title: "This is the title of the review",
    description: "This is what review says."
  }){
    id
    foodItemId
    consumerId
    rating
    title
    description
    dateCreated
    dateUpdated
  }
}