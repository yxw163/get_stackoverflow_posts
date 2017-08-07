 $(function() {
     Vue.filter('myDate', function(value) {
         var date = new Date(value * 1000)
         year = date.getFullYear()
         month = date.getMonth()
         day = date.getDate()
         hour = date.getHours()
         minute = date.getMinutes()
         seconds = date.getSeconds()
         Y = year + '-',
             M = ((month + 1) > 9 ? (month + 1) : ('0' + (month + 1))) + '-'
         D = (day > 9 ? day : ('0' + day)) + ' '
         h = (hour > 9 ? hour : ('0' + hour)) + ':'
         m = (minute > 9 ? minute : ('0' + minute)) + ':'
         s = (seconds > 9 ? seconds : ('0' + seconds))
         formatDate = Y + M + D + h + m + s
         return formatDate
     })

     var vm = new Vue({
         el: '#vm',
         data: {
             userId: '',
             userPosts: {},
             loadding: false,
             countOfPage: 5,
             currPage: 1,
             currPageContent: [],
             messageClass: 'uk-input uk-form-width-medium',
             hasPosts: false,
             errorFlag: false,
             errorText: 'User Id'
         },
         methods: {
             submit: function(event) {
                 event.preventDefault();
                 if (!this.userId.trim()) {
                     this.messageClass = 'uk-input uk-form-width-medium uk-form-danger'
                     this.errorText = 'Need a User Id'
                     return
                 }
                 this.loadding = true
                 this.messageClass = 'uk-input uk-form-width-medium'
                 this.$http.post('/userposts', {
                         userId: this.userId.trim()
                     })
                     .then((response) => {
                         this.loadding = false
                         this.userPosts = response.data
                         if (response.data.error_id) {
                             this.hasPosts = false
                             this.errorFlag = false
                             this.currPageContent = []
                         } else {
                             if (response.data.items.length != 0) {
                                 this.hasPosts = true
                                 this.errorFlag = false
                                 this.currPageContent = response.data.items.slice(0, 5)
                             } else {
                                this.hasPosts = false
                                this.errorFlag = true
                                this.currPageContent = []
                             }
                         }
                     });
             },
             setPage: function(idx) {
                 if (idx <= 0 || idx > this.totalPage) {
                     return
                 }
                 this.currPage = idx
                 this.currPageContent = this.userPosts.items.slice(idx * this.countOfPage - 1, (idx + 1) * this.countOfPage - 1)
             }
         },
         computed: {
             pageStart: function() {
                 return (this.currPage - 1) * this.countOfPage;
             },
             totalPage: function() {
                 if (this.userPosts.items) {
                     return Math.ceil(this.userPosts.items.length / this.countOfPage)
                 }
             }
         }
     });
     $('#vm').show();
 });
