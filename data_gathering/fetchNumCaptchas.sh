# usage ./fetchNumCatchas {number you want}
# will output captchas in captchas/ directory

if [ ! -d "$captchas" ]; then
    mkdir captchas
fi

for((i=0;i<$1;i+=1));
do
    #echo $i
    if [ $i -lt 10 ]; then
	c='c00'$i'.png'
    elif [ $i -lt 100 ]; then
	c='c0'$i'.png'
    else
	c='c'$i'.png'
    fi
    wget -q https://projecteuler.net/captcha/show_captcha.php -O captchas/$c &
    sleep .01
done
