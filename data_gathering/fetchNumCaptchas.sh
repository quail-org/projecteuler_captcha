# usage ./fetchNumCatchas {number you want}
# will output captchas in captchas/ directory

if [ ! -d "$captchas" ]; then
    mkdir captchas
fi

for((i=1;i<=$1;i+=1));
do
    echo $i
    c='c'$i'.png'
    wget https://projecteuler.net/captcha/show_captcha.php -O captchas/$c
done
