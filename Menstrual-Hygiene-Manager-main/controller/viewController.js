const getBlog = (req, res) => {
 
    res.render("blog.ejs");
 
};
const getCart = (req, res) => {
 
    res.render("cart.ejs");
 
};
const getLanding = (req, res) => {
  res.render("landing.ejs");
};
const getpamper = (req, res) => {
 
    res.render("pamperBooth.ejs");
 
};
const getProducts = (req, res) => {
 
    res.render("products.ejs");
 
};
const getSignin = (req, res) => {
    // res.redirect("/")
  
    res.redirect("signIn.ejs");
  
};
const getTracker = (req, res) => {
 
    res.render("tracker.ejs");
 
};
const getProfile = (req, res) => {
 
    res.render("userProfile.ejs");
 
};
const getForum = (req, res) => {
 
    res.render("forum.ejs")
 
};
 
const getConnect = (req,res)=>{
 
    res.render("call.ejs");
 
}
const login = (req,res)=>{
 
    res.render("LogIn.ejs");
 
}
const signup = (req,res)=>{
 
    res.render("signUp.ejs");
 
}
const getVideoCall = (req, res) => {
 
    res.render("videoCall.ejs");
 
};
 
module.exports = {
    getBlog,
    getCart,
    getLanding,
    getProducts,
    getpamper,
    getSignin,
    getTracker,
    getProfile,
    getForum,
    getConnect,
    login,
    signup,
    getVideoCall
}
