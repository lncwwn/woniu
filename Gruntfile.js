module.exports = function(grunt) {
    grunt.initConfig({
        less: {
            development: {
                options: {
                    paths: ['assets/less']
                },
                files: {
                    'assets/css/style.css': 'assets/less/style.less',
                    'assets/css/login.css': 'assets/less/login.less',
                    'assets/css/signup.css': 'assets/less/signup.less',
                    'assets/css/profile.css': 'assets/less/profile.less'
                }
            }
        },
        watch: {
            less: {
                files: ['assets/less/*.less'],
                tasks: ['less']
            },
            /*js: {
                files: ['assets/js/*.js'],
                tasks: ['webpack']
            }*/
        }

    });

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-less');
};
